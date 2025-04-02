# Building a World Map - eq_world_map.py
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')

# A Different Way of Specifying Chart Data - eq_world_map.py
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')

# Customizing Marker Size - eq_world_map.py
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{'size': [5*int(mag) for mag in mags]},
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')

# Customizing Marker Color - eq_world_map.py
# Customizing Marker Color - eq_world_map.py
import json

from adodbapi.apibase import NullTypes
from fontTools.misc.cython import returns
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day.json'
with open(filename, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    if eq_dict['properties']['mag']:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
    else:
        print("No mag")

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_earthquakes.html')
