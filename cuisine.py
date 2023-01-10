import folium
import pandas as pd
from folium import plugins
import PIL.Image
from PIL import Image
import sys
import os
import PIL.ExifTags
import math as m
import numpy as np

#data_path = "amenities-vancouver.json"
data_path = "combined_data.json"
all_data = pd.read_json(data_path,lines=True)
#print(all_data)
#all_data.tail()

cuisine = all_data.tags.apply(lambda x: pd.Series(x,  index=['cuisine']))
#cuisinefinal = cuisine.dropna()

df3 = pd.concat([all_data,cuisine],axis = 1)
d3=df3.dropna(subset=['cuisine'])

#cuis = d3.drop(['timestamp','amenity', 'tags'], axis =1)

cuis = d3.drop(['amenity', 'tags'], axis =1)

def get_latlong(filename):
    img = Image.open(filename)
    exif = {
        
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    return exif['GPSInfo']
#x = 'IMG_0520.JPG'
x = sys.argv[1]
info = get_latlong(x)

#print(info)

north = info[2]
east = info[4]

lat = ((((north[0] *60) + north[1]) *60) +north[2]) / 60 / 60 
long = -((((east[0] *60) + east[1]) *60) +east[2]) / 60 / 60 

lat, long = float(lat), float(long)

#print(lat)
#print(long)

def distance(data):
    R = 6371
    img_lat = data['user_lat']
    img_lon = data['user_long']
    dest_lat = data['lat']
    dest_lon = data['lon']
    lat_diff = (img_lat - dest_lat)
    lon_diff = (img_lon- dest_lon) 
    deg_lat = np.deg2rad(lat_diff)
    deg_lon = np.deg2rad(lon_diff)
    
    a = m.sin(deg_lat/2) * m.sin(deg_lat/2) + m.cos(np.deg2rad(img_lat)) * m.cos(np.deg2rad(dest_lat)) * m.sin(deg_lon/2) * m.sin(deg_lon/2)
    c = 2 *m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = R * c 
    return d

added = cuis.assign(user_lat=lat)
find = added.assign(user_long=long)

bycuis = find.groupby(['cuisine']).mean()
#bycuis
bycuis['distance'] = bycuis.apply(distance,axis =1)



#print(bycuis)
#bycuis = bycuis.drop(['lat','long','user_lat','user_long'])
cuisine_rec = bycuis[bycuis['distance'] < 0.5]
cuis_rec = cuisine_rec.drop(['lat','lon','user_lat','user_long'], axis = 1)
print("Recommended Cuisine:", cuis_rec)





