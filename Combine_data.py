import pandas as pd 


clean_amenities = pd.read_json('amenities-vancouver.json',lines =True)
#print(clean_amenities)


#tourism_path = "../code/tourism_data.json"
tourism_data = pd.read_json('tourism_data.json', lines=True)

hotel_data = pd.read_json('hotel_data.json', lines=True)


combined_data = clean_amenities.append(tourism_data,ignore_index = True)
combined_data = combined_data.append(hotel_data, ignore_index =True)
combined_data = combined_data.drop(columns=['timestamp'])
combined_data = combined_data.dropna(subset=['name'])
#print(combined_data)
#combined_data_path = "../code/combined_data.json.gz"
combined_data.to_json('combined_data.json', orient = 'records', lines=True)
