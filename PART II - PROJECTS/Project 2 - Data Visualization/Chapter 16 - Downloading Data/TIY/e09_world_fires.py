# 16-09 World Fires - e09_world_fires.py
import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    fires, lons, lats, dates = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            lats.append(row[0])
            lons.append(row[1])
            fires.append(int(row[2]))

        except ValueError:
            print(f"Missing data for {current_date}")

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    'marker':{
        'size': [0.1 * fire for fire in fires],
        'color': fires,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Fire Strength'},
    },
}]

my_layout = Layout(title='Wildfires Worldwide')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig,filename='global_fires.html')