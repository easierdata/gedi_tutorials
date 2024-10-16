# Tutorials on GEDI Science Data Products

**Author:** ORNL DAAC & EASIER Data       
**Date:** August 26, 2021       
**Updated on:** October 1, 2024       
**Contact for the ORNL DAAC:** uso@daac.ornl.gov       
**Contact for EASIER Data:** toshan@umd.edu       
**Keywords:** lidar, GEDI, AGBD, aboveground biomass, IPFS, Filecoin       


## Overview      
These tutorials demonstrate how to discover, access, and use [GEDI science data products](https://daac.ornl.gov/gedi) from decentralized sources such as [IPFS](https://docs.ipfs.tech/concepts/what-is-ipfs/). The GEDI collection is maintained and archived at the ORNL DAAC. GEDI L3, L4A, and L4B data products are available from decentralized and centralized sources as noted in [various data tools and services](services.md).

## Getting Started: Clone repo and deploy poetry project

This project uses [Poetry](https://python-poetry.org/) for dependency management and is compatible with python versions >=3.11. To install all necessary dependencies, follow these steps:

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

4. Generate the configuration file

    ```shell
    poetry run edit-config
    ```

5. Run Jupyter Notebook and start with a tutorial.
    
    ```shell
    poetry run jupyter notebook
    ``` 

## GEDI L4A Footprint Level Aboveground Biomass Density
### :green_book: Jupyter Notebooks 
1. [Search and download GEDI L4A dataset](1_gedi_l4a_search_download.ipynb): search and download GEDI L4A granules over an area of interest to a local machine
1. [Subset GEDI L4A footprints](2_gedi_l4a_subsets.ipynb): subset downloaded GEDI L4A granules to an area of interest
1. [Explore GEDI L4A data structure](3_gedi_l4a_exploring_data.ipynb): explore data structure, variables, and quality flags of the GEDI L4A dataset. 
1. [Direct S3 Access GEDI L4A from the NASA EarthData Cloud](gedi_l4a_direct_s3_access.ipynb): retrieve the GEDI L4A dataset from NASA Earthdata Cloud using direct S3 access. 
1. [Access GEDI L4A dataset with NASA OPeNDAP in the Cloud](access_gedi_l4a_hyrax.ipynb): access selected variables for the GEDI L4A dataset within an area of interest using OPeNDAP Hyrax 
1. [Access GEDI L4A dataset with NASA Harmony API](gedi_l4a_harmony.ipynb): direct access and subset the GEDI L4A variables using NASA Harmony API 
1. [Reproduce L4A AGBD estimates from GEDI L2A RH metrics](reconstruct_L4A_AGBD_L2A_metrics.ipynb): reconstruct L4A AGBD estimates using L2A relative height (RH) metrics
1. [Apply correction to AGBD estimates for selected L4A shots, Version 2](correct_GEDI_L4A_V002_01.ipynb): apply AGBD correction to Version 1 (V001) GEDI L4A shots affected with the algorithm setting group 10 issue


| :red_mark: MARKED FOR POSSIBLE REMOVAL :red_mark: |
### :computer: Python Scripts
1. [Search and download GEDI L4A dataset](scripts#1-gedi_l4a_search_downloadpy): downloads GEDI L4A granules to a local directory based on GeoJSON polygon 
1. [Subset GEDI L4A footprints](scripts#2-gedi_l4a_subsetspy): subsets the downloaded GEDI L4A granules by a GeoJSON polygon file
1. [Subset GEDI L4A with NASA OPeNDAP in the Cloud](scripts#3-gedi_l4a_hyraxpy): accesses the GEDI L4A dataset using NASA's OPeNDAP Hyrax

| :red_mark: MARKED FOR POSSIBLE REMOVAL :red_mark: |
## GEDI L4B Gridded Aboveground Biomass Density
### :green_book: Jupyter Notebooks
1. [Access GEDI L4B Dataset with OGC Web Services](https://nbviewer.org/github/ornldaac/gedi_tutorials/blob/main/gedi_l4b_ogc.ipynb): visualize and access the GEDI L4B dataset using the OGC WMS and WCS services

## Related Resources

- Learn about the EASIER Data Initiative: [Easier Data](https://easierdata.org/about)
- NASA Earthdata Webinar: [Explore NASA GEDI Aboveground Biomass Datasets, Services, and Tools at NASA's ORNL DAAC](https://daac.ornl.gov/resources/tutorials/2022_earthdata_webinar/)
- ESA Workshop: [Synergistic Use of SAR and Lidar Data for Terrestrial Ecology Research](https://daac.ornl.gov/resources/workshops/esa-2021-workshop/)

More resources related to ORNL DAAC data and web services can be found at the [ORNL DAAC Learning](https://daac.ornl.gov/resources/learning/) page.