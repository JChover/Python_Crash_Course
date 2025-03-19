# 15-10 Practicing with Both Libraries - e10_randomwalk_plotly.py
import plotly.graph_objs as go
from plotly import offline

from e03_random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(50_000)  # Increase number of points to 50,000
rw.fill_walk()

# Create scatter plot for the points in the walk
point_numbers = range(rw.num_points)
scatter_trace = go.Scatter(x=rw.x_values, y=rw.y_values)

# Create the figure and add traces
fig = go.Figure(data=[scatter_trace])

# Update layout to remove axes
fig.update_layout(
    title='Random Walk (50,000 Steps)',
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    showlegend=False,
    width=800,
    height=600
)

# Show the plot
offline.plot(fig)
