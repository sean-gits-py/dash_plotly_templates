import pandas as pd
import plotly.express as px
import numpy as np

# Generate some sample lat/lon data for San Diego
np.random.seed(42)
n_points = 1000
latitudes = np.random.uniform(32.6, 32.9, n_points)
longitudes = np.random.uniform(-117.3, -116.9, n_points)

# Create a DataFrame with sample latitude and longitude data
data = pd.DataFrame({'lat': latitudes, 'lon': longitudes})

# Create the hexbin density map using Plotly Express
fig = px.density_mapbox(
    data, 
    lat='lat', 
    lon='lon', 
    radius=10,
    center=dict(lat=32.7157, lon=-117.1611), # Center on San Diego
    zoom=10,
    mapbox_style='carto-positron'
)

# Show the figure
fig.show()
