# Python scripts

## 1. gedi_l4a_search_download.py

This script downloads GEDI L4A granules to a local directory based on GeoJSON polygon and start/end dates. First, set up NASA Earthdata Login authentication using a `.netrc` file. Please refer to the instructions here: https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+cURL+And+Wget. 

### usage
```bash
./gedi_l4a_search_download.py --doi <DOI> --date1 <start_date> --date2 <end_date> --poly <path_to_geojson_file> --outdir <path_to_directory>
```
### arguments
| argument  | description |
| ------------- | ------------- |
| --help  |  show help message and exit  |
| --doi | dataset DOI e.g., 10.3334/ORNLDAAC/2056 for GEDI L4A V2.1 |
| --date1 | start date in YYYY-MM-DD format |
| --date2 | end date in YYYY-MM-DD format |
| --poly | path to a GeoJSON file defining area of interest|
| --outdir | path to the directory for saving downloaded h5 files |

### example usage

```bash
./gedi_l4a_search_download.py --date1 2019-12-15 --date2 2020-01-12 --doi 10.3334/ORNLDAAC/2056 --poly ../polygons/amapa.json --outdir ../full_orbits/
```

## 2. gedi_l4a_subsets.py

This script subsets the downloaded GEDI L4A granules by a GeoJSON polygon file. The output files are in the H5 native format, with the option of converting to CSV or GeoJSON formats, and include the GEDI shots within the bounds of the polygon file. 

### usage
```bash
./gedi_l4a_subsets.py --poly <path_to_geojson_file> --indir <path_to_input_directory> --subdir <path_to_output_directory> [--csv] [--json]
```
### arguments
| argument  | description |
| ------------- | ------------- |
| --help  |  show help message and exit  |
| --poly | path to a GeoJSON file defining area of interest|
| --indir | path to the directory with downloaded h5 files |
| --subdir | path to the directory for saving subset files |
| --csv | (optional) setting this creates additional output CSV subset file |
| --json | (optional) setting this creates additional output GeoJSON subset file |

### example usage

```bash
./gedi_l4a_subsets.py --poly ../polygons/amapa.json --indir ../full_orbits/ --subdir ../subsets/ --csv
```


## 3. gedi_l4a_hyrax.py
This script accesses the GEDI L4A dataset using [NASA's OPeNDAP Hyrax](https://opendap.earthdata.nasa.gov/). First, set up NASA Earthdata Login authentication using a `.netrc` file. Please refer to the instructions here: https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+cURL+And+Wget. 

### usage
```bash
./gedi_l4a_hyrax.py --doi <DOI> --date1 <start_date> --date2 <end_date> --poly <path_to_geojson_file> --beams <gedi_beams> --variables <gedi_variables> --outfile <output_CSV_filename> [--json]
```
### arguments
| argument  | description |
| ------------- | ------------- |
| --help  |  show help message and exit  |
| --doi | dataset DOI e.g., 10.3334/ORNLDAAC/2056 for GEDI L4A V2.1 |
| --date1 | start date in YYYY-MM-DD format |
| --date2 | end date in YYYY-MM-DD format |
| --poly | path to a GeoJSON file defining area of interest |
| --beams | GEDI beam names in a comma-separated format |
| --variables | GEDI variable names in a comma-separated format |
| --outfile | output CSV file name |
| --json | (optional) setting this creates additional GeoJSON output file |

### example usage

```bash
./gedi_l4a_hyrax.py --doi 10.3334/ORNLDAAC/2056 --date1 2019-12-15 --date2 2020-01-12 --poly ../polygons/amapa.json --beams BEAM0101,BEAM0110,BEAM1000,BEAM1011 --variables agbd,agbd_t,agbd_t_se,l4_quality_flag,land_cover_data/pft_class --outfile ../subsets/amapa_l4a_hyrax.csv
```

## 4. poetry_cmds.py
This script contains a set of defined command functions that are called with with the [`run` command](https://python-poetry.org/docs/cli#run) from poetry. Here are the available commands:

- **edit-config**: Modify the configuration file interactively through the command line.
- **print-config**: Print the default configuration file.
- **reset-config**: Reset the configuration file back to the default settings.
- **check-config**: Check that the configuration file is valid and that the IPFS and STAC endpoints are reachable.

### usage
```bash
poetry run <command>
```

## 5. easier_utils.py
This script contains a set of utility functions that are reused across the notebooks and scripts in this repository. 