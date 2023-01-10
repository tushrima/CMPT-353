import pandas as pd 
import numpy as np
import math as m




def distance(data):
	R = 6371
	img_lat = data['Img_lat']
	img_lon = data['Img_lon']
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
