import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.cluster import KMeans
import plotly.express as px

#data_path = "combined_da.json.gz"

all_data = pd.read_json("combined_data.json", lines=True)
#print(all_data)
#all_data.head()

#fast_food = all_data[all_data['amenity'] == "fast_food"]
restro_bars = all_data[(all_data['amenity'] == "cafe") | 
    (all_data['amenity'] == 'fast_food') | 
    (all_data['amenity'] == 'restaurant')|
    (all_data['amenity'] == 'bistro')]

#print(restro_bars)

restro_bars = restro_bars.drop(['tags'], axis=1)
restr_bars = restro_bars.dropna(subset='name')

chain_rest = restro_bars[restro_bars.duplicated('name', keep =False)]
#print(chain_rest['name'])
#fig = px.scatter_geo(fast_food,lat='lat',lon='lon', hover_name="name")
fig = px.density_mapbox(chain_rest, lat='lat', lon='lon', hover_name='name', radius=10,
                        center=dict(lat=49.2, lon=-123.1), zoom=10, height=800, width=800,
                        mapbox_style="stamen-terrain")
fig.update_layout(title = 'World map', title_x=0.5)
fig.write_image("Chain_rest.svg")


non_chain = restro_bars.drop_duplicates('name', keep =False)
#print(non_chain['name'])

fig = px.density_mapbox(non_chain, lat='lat', lon='lon', hover_name='name', radius=10,
                        center=dict(lat=49.2, lon=-123.1), zoom=10, height=800, width=800,
                        mapbox_style="stamen-terrain")
fig.update_layout(title = 'World map', title_x=0.5)
fig.write_image("NonChain_rest.svg")
bar_rest = {'Chain restaurants': chain_rest.count(), 'Non-Chain restaurant': non_chain.count()}
rest = list(bar_rest.keys())
values =list(bar_rest.values())

#print(restro_bars[[cuisine]])
#plt.bar(rest, values)
#plt.show()
