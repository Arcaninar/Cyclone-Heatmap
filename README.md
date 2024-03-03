# Cyclone Heatmap

> Data Analysis of Japan's Cyclone
<hr>

This is a project that analyses Japan's Cyclone data from 2000 - 2022. The raw data is from [Japan Meteorological Agency](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html), which also includes the format of the data.

## Project Output

* Heatmaps with interactive widgets
* Excel files containing statistics of each cyclone
* Heatmap timelapse in .gif format

## Project Contents

In total, there are 5 IPython Notebook files:
* **Data_Cleaning**. Transforms raw_data.txt to heatmap_data.txt which will be used in Cyclone_Heatmap & Heatmap_to_GIF_timelapse notebooks.
* **Raw_Data_to_Excel**. Transforms raw_data.txt to Excel Files
* **Cyclone_Statistics**. Transforms raw_data.txt to some useful statistics like minimum, maximum, & average of the cyclone's latitude, longitude, wind speed, and pressure
* **Cyclone_Heatmap**. Creates an interactive heatmap from heatmap_data.txt
* **Heatmap_to_GIF_timelapse**. Creates a heatmap timelapse

## Heatmap Timelapse Preview
![Heatmap Timelapse](https://github.com/Arcaninar/Cyclone-Heatmap/blob/main/Heatmap_Timelapse.gif)

## How to run this project
1. Clone this project
2. Setup a Python kernel (I used [Anaconda Python kernel](https://docs.anaconda.com/free/anaconda/install/windows/) and the [online Jupyter Notebook](https://saturncloud.io/blog/how-to-add-a-library-in-jupyter-notebook-online/))
3. Install these Python libraries
   * [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
   * Folium [(Pip)](https://pypi.org/project/folium/) [(Anaconda)](https://anaconda.org/conda-forge/folium)
   * [Ipywidgets](https://ipywidgets.readthedocs.io/en/stable/user_install.html)
   * [GrabzIt](https://grabz.it/api/python/download/)
   * [Imageio](https://imageio.readthedocs.io/en/stable/user_guide/installation.html)
   * Pathlib [(Pip)](https://pypi.org/project/pathlib/) [(Anaconda)](https://anaconda.org/anaconda/pathlib)
4. Open the needed .ipynb file using a rich text editor like VSCode, or an IDE.
5. Run all the code cells on that .ipynb file

## Contributor
This is a personal project which I intend to stop here. If you want to edit this project, you can clone it to your own GitHub repository
