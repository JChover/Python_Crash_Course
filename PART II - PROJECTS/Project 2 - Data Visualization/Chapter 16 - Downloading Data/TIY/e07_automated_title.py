# 16-07 Automated Title - e07_automated_title.py
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

metadata = all_eq_data['metadata']
file_title = metadata['title']
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict['properties']['mag']:
        mags.append(eq_dict['properties']['mag'])
        lons.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])
    else:
        print("No magnitude.")

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=file_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')