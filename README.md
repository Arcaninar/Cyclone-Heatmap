# Cyclone Heatmap

> Data Analysis of Japan's Cyclone
<hr>

This is a project that analyses Japan's Cyclone data from 2000 - 2022. The raw data is from [Japan Meteorological Agency](https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html), which also includes the format of the data. This project creates Heat maps, Excel files, and a Heatmap GIF timelapse. All the code is in the separate IPython Notebook file.

## Project Contents

In total, there are 5 IPython Notebook files:
* **Data_Cleaning**. Transforms raw_data.txt to heatmap_data.txt which will be used in Cyclone_Heatmap & Heatmap_to_GIF_timelapse notebooks.
* **Raw_Data_to_Excel**. Transforms raw_data.txt to Excel Files containing statistics of each cyclone
* **Cyclone_Statistics**. Transforms raw_data.txt to some useful statistics like minimum, maximum, & average of the cyclone's latitude, longitude, wind speed, and pressure
* **Cyclone_Heatmap**. Creates a heatmap from heatmap_data.txt
* **Heatmap_to_GIF_timelapse**. Creates a timelapse of the heatmap in .gif format

## Heatmap Example
