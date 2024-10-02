# Print out a list of properties and methods available to the client object but disregard any of the `__` properties. Additionally,  Specify what's a property and whats a method.
# Identify the client object with the longest name
def print_properties(obj):
    prop_with_longest_name = max(
        [attr for attr in dir(obj) if not attr.startswith("__")], key=len
    )

    # Print out header with the name of the object that we are inspecting
    print(f"Properties and methods of {type(obj)} object:\n")

    max_padding = len(prop_with_longest_name) + 2
    # Create named tuple to store object properties
    properties = []
    for attr in dir(obj):
        if not attr.startswith("__"):
            print(f"{attr.ljust(max_padding)}: {type(getattr(obj, attr))}")
            properties.append((attr, type(getattr(obj, attr))))
    return properties


def print_granule_properties(granule):
    def max_widths(indexes):
        max_widths = []
        for i in range(len(indexes[0])):
            max_widths.append(max(len(str(idx[i])) + 2 for idx in indexes))
        return max_widths

    # Convert pystac object to dictionary
    # granule = granule_results.items[0].to_dict()
    granule_properties = []  #

    for key, value in granule.to_dict().items():
        if isinstance(value, dict):
            granule_properties.append((key, type(value), ""))
        elif isinstance(value, list):
            granule_properties.append((key, type(value), ""))
        elif isinstance(value, str):
            granule_properties.append((key, type(value), value))
        else:
            granule_properties.append((key, value, type(value)))

    widths = max_widths(granule_properties)

    # Print the results into a formatted table
    print("Property Name".ljust(widths[0]), "Type".ljust(widths[1]), "Value")
    print("-" * sum(widths))
    for prop in granule_properties:
        print(
            str(prop[0]).ljust(widths[0]), str(prop[1]).ljust(widths[1]), str(prop[2])
        )
    print("-" * sum(widths))

    print(
        """\n
For our purpose, we want to take a look at the `assets` property of the granule. Each item in `assets` contains 
additional properties like the file name, type and what locations the data can be retrieved from.
      
Expand the `alternate` property below to see where it can be sourced from.
      """
    )


def get_cid_payload(granule):

    granule_cid_payload = {}
    for g in granule:
        # Grab the asset we want based on values in the key
        selected_asset_key = [
            source for source in g.assets.keys() if "gov/protected" in source
        ][0]

        # Grab the the source IPFS from the `alternate` property
        ipfs_source = g.assets[selected_asset_key].to_dict()["alternate"]["IPFS"]
        cid = ipfs_source["href"].split("/")[-1]

        # Append the granule CID and pystac Item object to the dictionary
        granule_cid_payload[g.id] = {
            "cid": cid,
            "item": g,
            "asset_key": selected_asset_key,
            "file_name": g.id.split(".", 1)[-1],
        }

    return granule_cid_payload


def print_granule_metadata(client_obj, cid):
    import h5py
    import tabulate
    from io import BytesIO
    from IPython.display import HTML, display

    with h5py.File(BytesIO(client_obj.getFromCID(cid)), "r") as hf:
        # read the METADATA group
        metadata = hf["METADATA/DatasetIdentification"]
        # store attributes and descriptions in an array
        data = []
        for attr in metadata.attrs.keys():
            data.append([attr, metadata.attrs[attr]])

        # display `data` array as a table
        tbl_n = 1  # table number
        print("\n")
        print(f"Table {tbl_n}. Attributes and discription from `METADATA` group")
        headers = ["attribute", "description"]
        display(HTML(tabulate.tabulate(data, headers, tablefmt="html")))


def compare_search_results(cmr_granules: list, stac_granules: list):

    if len(cmr_granules) == len(stac_granules):
        print(
            "Excellent! All the requested items from the CMR appear in our STAC query."
        )

    elif len(cmr_granules) > len(stac_granules):
        print("There is a discrepancy in the number of items returned")
        # get a list of the  granule IDs that are missing from the STAC query

        missing_granules = [
            granule_id for granule_id in cmr_granules if granule_id not in stac_granules
        ]
        if len(missing_granules) > 0:
            print(
                f"The STAC query is missing the following granules: {missing_granules}"
            )

    # Compare the number of items returned from the CMR and STAC queries
    elif len(stac_granules) > len(cmr_granules):
        # get a list of the granule IDs that are missing from the STAC query
        granules_to_remove = [
            granule_id for granule_id in stac_granules if granule_id not in cmr_granules
        ]
        if len(granules_to_remove) > 0:
            print(f"The STAC query has {len(granules_to_remove)} extra granules.")
