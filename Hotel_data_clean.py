import pandas as pd
import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
def create_Tag(data):
	tags = {}
	tags['website'] = data['Website']
	return tags


def main(inputs, outputs):
	hotel_data= pd.read_csv(inputs)
	new_data=pd.DataFrame()
	new_data['lat'] = hotel_data['Latitude']
	new_data['lon'] = hotel_data['Longitude']
	new_data['amenity'] = hotel_data['Product_Group']
	new_data['name'] = hotel_data['Product_Name']
	new_data['tag'] =  (hotel_data.apply(create_Tag, axis=1))
	new_data = new_data.where((new_data['lon'] > -123.5) & (new_data['lon'] < -122))
	new_data = new_data.where((new_data['lat'] > 49) & (new_data['lat'] < 49.5))
	new_data = new_data.dropna()
	#print(new_data)
	
	new_data.to_json(outputs, orient = 'records', lines=True )
	
if __name__ == '__main__':
    inputs = sys.argv[1]
    output = sys.argv[2]
    main(inputs, output)