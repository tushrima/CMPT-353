import PIL.Image
from PIL import Image
import sys
import os

import PIL.ExifTags
def get_latlong(filename):
    img = filename
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    return exif['GPSInfo']


#x = "IMG_1266.jpg"
#x = Image.open(sys.argv[1])

def get_img_Coordinates(x):
    info = get_latlong(x)
    #print(info)
    north = info[2]
    east = info[4]
    lat = ((((north[0] *60) + north[1]) *60) +north[2]) / 60 / 60 
    long = -((((east[0] *60) + east[1]) *60) +east[2]) / 60 / 60 
    coord = float(lat), float(long)
    #return lat , long
    #print(lat)
    return coord

#get_img_Coordinates(x)
#from gmplot import gmplot
#gmap = gmplot.GoogleMapPlotter(lat, long, 12)
#gmap.marker(lat, long, "cornflowerblue")
#gmap.draw("location.html")






