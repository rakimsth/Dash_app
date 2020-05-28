import pandas as pd
import numpy as np
import os
import dash_html_components as html
import dash_core_components as dcc
import dash
import plotly.express as px
import plotly.graph_objects as go


# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
st = pd.read_csv('dailyload5zone.csv')

# Step 3. Create a plotly figure
trace_1 = go.Scatter(x=st.datetime, y=st['zone_1'],
                     name='zone_1',
                     line=dict(
                         width=2, color='rgb(229, 151, 50)'))
layout = go.Layout(title='Time Series Plot',
                   hovermode='closest')
fig = go.Figure(data=[trace_1], layout=layout)

# Step 4. Create a Dash layout
app.layout = html.Div([
    dcc.Graph(id='plot', figure=fig)
])

# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug=True)

# # Turn off reloader if inside Jupyter
# app.run_server(debug=True, use_reloader=True)
