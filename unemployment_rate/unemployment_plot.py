import plotly.graph_objs as go
import pandas as pd
from fredapi import Fred
from keys import FRED_API_KEY
import os

# FRED API key
# FRED_API_KEY = os.getenv('FRED_API_KEY')  # Replaced with keys.py variable
fred = Fred(api_key=FRED_API_KEY)

# List of state unemployment rate series IDs
state_series_ids = {
    'Alabama': 'ALUR',
    'Alaska': 'AKUR',
    'Arizona': 'AZUR',
    'Arkansas': 'ARUR',
    'California': 'CAUR',
    'Colorado': 'COUR',
    'Connecticut': 'CTUR',
    'Delaware': 'DEUR',
    'District of Columbia': 'DCUR',
    'Florida': 'FLUR',
    'Georgia': 'GAUR',
    'Hawaii': 'HIUR',
    'Idaho': 'IDUR',
    'Illinois': 'ILUR',
    'Indiana': 'INUR',
    'Iowa': 'IAUR',
    'Kansas': 'KSUR',
    'Kentucky': 'KYUR',
    'Louisiana': 'LAUR',
    'Maine': 'MEUR',
    'Maryland': 'MDUR',
    'Massachusetts': 'MAUR',
    'Michigan': 'MIUR',
    'Minnesota': 'MNUR',
    'Mississippi': 'MSUR',
    'Missouri': 'MOUR',
    'Montana': 'MTUR',
    'Nebraska': 'NEUR',
    'Nevada': 'NVUR',
    'New Hampshire': 'NHUR',
    'New Jersey': 'NJUR',
    'New Mexico': 'NMUR',
    'New York': 'NYUR',
    'North Carolina': 'NCUR',
    'North Dakota': 'NDUR',
    'Ohio': 'OHUR',
    'Oklahoma': 'OKUR',
    'Oregon': 'ORUR',
    'Pennsylvania': 'PAUR',
    'Rhode Island': 'RIUR',
    'South Carolina': 'SCUR',
    'South Dakota': 'SDUR',
    'Tennessee': 'TNUR',
    'Texas': 'TXUR',
    'Utah': 'UTUR',
    'Vermont': 'VTUR',
    'Virginia': 'VAUR',
    'Washington': 'WAUR',
    'West Virginia': 'WVUR',
    'Wisconsin': 'WIUR',
    'Wyoming': 'WYUR'
}

# Get unemployment rate data for each state and prepare traces for Plotly
traces = []

for state, series_id in state_series_ids.items():
    try:
        data = fred.get_series(series_id)
        trace = go.Scatter(x=data.index, y=data.values, mode='lines', name=state)
        traces.append(trace)
    except Exception as e:
        print(f"Could not retrieve data for {state}: {e}")

# Create the layout for the plot
layout = go.Layout(
    title='Unemployment Rates for All States',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Unemployment Rate (%)'),
    legend=dict(font=dict(size=10)),
    height=800
)

# Create the figure and plot it
fig = go.Figure(data=traces, layout=layout)
fig.show()
