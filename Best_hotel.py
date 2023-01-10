import pandas as pd 
import numpy as np
import sys
from Distance import distance 
from Img_coord import get_img_Coordinates
import PIL.Image
from PIL import Image
import plotly.express as px
import folium 
from folium import plugins

def main(image):

	amenities_data = pd.read_json("combined_data.json", lines=True )

	amenities = amenities_data.drop_duplicates(subset = ['amenity'], keep = 'first') 
	amenities = amenities.reset_index(drop = True)
	amenities['amenity'].to_csv("list_amenties.csv")
	

	img_coordinate = get_img_Coordinates(image)

	print("The coordinates of the img uploaded: " + str(img_coordinate) + "\n")
	amenities_data = amenities_data.assign(Img_lat = img_coordinate[0])
	amenities_data = amenities_data.assign(Img_lon = img_coordinate[1]) 

	amenities_data['distance'] = amenities_data.apply(distance, axis = 1) 
	best_hotels = amenities_data.sort_values(by = 'distance') 
	#print(best_hotels)
	best_hotels = best_hotels.where(best_hotels['amenity'] == 'Accommodation') 
	#print(best_hotels)
	best_hotels =best_hotels.dropna(subset=['name'])
	best_hotels = best_hotels.drop_duplicates(subset = ['name'],keep = 'first')
	print("Three Recommended Accomodation's near you:")

	best_hotels = best_hotels.head(3)
	best_hotels = best_hotels.reset_index(drop=True)
	print(best_hotels['name']) 
	

	hotel = best_hotels[['lat','lon']]
	hotellist = hotel.values.tolist()
	map = folium.Map(location=[49.25, -123.1], zoom_start=12)
	for point in range(0, len(hotellist)):
		folium.Marker(hotellist[point], popup=best_hotels['name'][point]).add_to(map)
	map.save('hotels.html')

	restro_bars = amenities_data[(amenities_data['amenity'] == "cafe") | 
		(amenities_data['amenity'] == 'fast_food') | 
		(amenities_data['amenity'] == 'restaurant')|
		(amenities_data['amenity'] == 'pub')|
		(amenities_data['amenity'] == 'ice_cream') |
		(amenities_data['amenity'] == 'bistro')]
	restro_bars = restro_bars.dropna(subset=['name'])
	restro_bars = restro_bars.drop_duplicates(subset = ['name'], keep = 'first')
	restro_bars = restro_bars.sort_values(by = 'distance')

	activities = amenities_data[(amenities_data['amenity'] == 'Activities_Attractions' )|
		(amenities_data['amenity'] == 'lounge')|
		(amenities_data['amenity'] == 'casino')|
		(amenities_data['amenity'] == 'hookah_lounge')|
		(amenities_data['amenity'] == 'spa')|
		(amenities_data['amenity'] == 'boat_rental')|
		(amenities_data['amenity'] == 'nightclub')|
		(amenities_data['amenity']== 'theatre' )|
		(amenities_data['amenity'] =='cinema')|
		(amenities_data['amenity'] == 'bicycle_rental')]
	activities = activities.dropna(subset=['name'])
	activities = activities.drop_duplicates(subset = ['name'], keep = 'first')
	activities = activities.sort_values(by='distance')

	print("Here are 10 of the best places to check out:")
	restro_bars = restro_bars.head(5)
	activities = activities.head(5)
	data = [activities,restro_bars]
	best_spots = pd.concat(data)
	best_spots = best_spots.sample(frac=1)
	best_spots = best_spots.reset_index(drop=True)

	print(best_spots[['name','amenity']])


if __name__ == '__main__':
    img = Image.open(sys.argv[1])
    main(img)



