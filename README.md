# Tutorials on GEDI Science Data Products

**Author:** ORNL DAAC & EASIER Data       
**Date:** August 26, 2021       
**Updated on:** October 1, 2024       
**Contact for the ORNL DAAC:** uso@daac.ornl.gov       
**Contact for EASIER Data:** toshan@umd.edu       
**Keywords:** lidar, GEDI, AGBD, aboveground biomass, IPFS, Filecoin       


## Overview      
These tutorials demonstrate how to discover, access, and use [GEDI science data products](https://daac.ornl.gov/gedi) from decentralized sources such as [IPFS](https://docs.ipfs.tech/concepts/what-is-ipfs/). The GEDI collection is maintained and archived at the ORNL DAAC. GEDI L3, L4A, and L4B data products are available from decentralized and centralized sources, as noted in [various data tools and services](services.md).

## Getting Started: Clone repo and deploy poetry project

This project uses [Poetry](https://python-poetry.org/) for dependency management and is compatible with Python versions >=3.11. To install all necessary dependencies, follow these steps:

1. Install Poetry if you haven't already:

   ```shell
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:

   ```shell
   git clone https://github.com/easierdata/gedi_tutorials.git
   cd gedi_tutorials
   ```

3. Install the dependencies:

   ```shell
   poetry install
   ```

4. Generate the configuration file by running the following command.

    ```shell
    poetry run edit-config
    ```

   > A file named `config.json` is generated in the root directory and can be modified by re-running the command. See this [page](scripts/README.md/#1-poetry_cmdspy) for more details on the available commands.

5. Run Jupyter Notebook and start with a tutorial.
    
    ```shell
    poetry run jupyter notebook
    ``` 

## GEDI L4A Footprint Level Aboveground Biomass Density
### :green_book: Jupyter Notebooks 
1. [Search and download GEDI L4A dataset](1_gedi_l4a_search_download.ipynb): search and download GEDI L4A granules over an area of interest to a local machine
2. [Subset GEDI L4A footprints](2_gedi_l4a_subsets.ipynb): subset downloaded GEDI L4A granules to an area of interest
3. [Explore GEDI L4A data structure](3_gedi_l4a_exploring_data.ipynb): explore data structure, variables, and quality flags of the GEDI L4A dataset. 


## Related Resources

- Learn about the EASIER Data Initiative: [Easier Data](https://easierdata.org/about)
- NASA Earthdata Webinar: [Explore NASA GEDI Aboveground Biomass Datasets, Services, and Tools at NASA's ORNL DAAC](https://daac.ornl.gov/resources/tutorials/2022_earthdata_webinar/)
- ESA Workshop: [Synergistic Use of SAR and Lidar Data for Terrestrial Ecology Research](https://daac.ornl.gov/resources/workshops/esa-2021-workshop/)

More resources related to ORNL DAAC data and web services can be found at the [ORNL DAAC Learning](https://daac.ornl.gov/resources/learning/) page.