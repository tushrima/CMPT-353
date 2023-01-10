# CMPT353
"In your repository's README (or README.md) file, you should document your code and how to run it: required libraries, commands (and arguments), order of execution, files produced/expected. You should do this because (1) you should always do that, and (2) to give us some hope of running your code."

Required libraries
-import PIL.Image
-from PIL import Image
-import sys
-import os
-import csv
-import PIL.ExifTags
-import folium
-import pandas as pd
-from folium import plugins
-import plotly.express as px
-import math as m


Order of Execution
python3 tourism_data_clean.py hellobc-attractions-listing-20221205.csv tourism_data.json
python3 hotel_data_clean.py hellobc-accommodation-listing-20221205.csv tourism_data.json
python3 Combine_data.py
python3 Best_hotel.py IMG_0520.py
open jupyter notebook -> open path.ipynb -> run each line to reach the desired output of the figure that shows the path taken
python3 cuisine.py IMG_0520.py


Files
-hellobc-accommodation-listing-20221205.csv : dataset from BC Data Catalogue
-hellobc-attractions-listing-20221205.csv : dataset from BC Data Catalogue
-tourism_data_clean.py : python file to extract data from hellobc-attractions-listing-20221205.csv to contain it to vancouver area and drop NULL
-tourism_data.json : .json file after implementing tourism_data_clean.py
-hotel_data_clean.py : python file to extract data from hellobc-accommodation-listing-20221205.csv to contain it to vancouver area and drop NULL
-hotl_data.json : .json file after implementing hotel_data_clean.py
-Combine_data.py : python file to append data from tourism_data.json, hotel_data.json, and amenities-vancouver.json
-Best_hotel.py : python file to answer Q1
-hotels.svg : outputs a visual of the vancouver map with top 3 hotels
-heat.py : python file to answer Q2, which provides 2 density heat maps; Chain_rest.svg & NonChain_rest.svg
-path.ipynb : jupyter notebook that outputs the entire path taken by the user from the tour
-cuisine.py : python file that recommends top cuisines that are nearby within 0.5
-img_coord.py : returns image coordinates used as a function and called in Best_hotel.py 
-picture.csv : currently has 5 images with latitude and longitude
-Distance.py : uses haversine function to calculate distance
