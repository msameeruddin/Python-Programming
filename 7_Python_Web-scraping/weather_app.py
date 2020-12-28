import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import dash_table as dt

from dash.dependencies import (Input, Output)
from loc_weather import WeatherApp

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True
app.title = 'Weather App'

app.layout = html.Div([
    html.Div([
        html.H2('Global Weather Application', style={'marginTop' : 30}),
        html.Div([
            dcc.Input(id='location-input', value='hyderabad', type='text', placeholder='City name: ', size='80', debounce=True),
        ], style={'marginTop' : 20}),
        html.Div([
            html.Div(id='output-map'),
        ]),
    ], style={'textAlign' : 'center'})
])

@app.callback(
    Output('output-map', 'children'),
    [Input('location-input', 'value')]
)
def get_weather_details(location):
    w_app = WeatherApp(location=location)
    loc_lat = [w_app.lat]
    loc_lon = [w_app.lon]
    description, celsius_temp, farenheit_temp, humidity, wind_speed, clouds = w_app.get_parsed_details()
    curated_location = w_app.location.title()

    df = pd.DataFrame()
    df['Details'] = ['Place', 'Description', 'Celsius Temp', 'Farenheit Temp', 'Humidity', 'Wind Speed (mpg)', 'Total Clouds']
    df['Info'] = [curated_location, description, celsius_temp, farenheit_temp, humidity, wind_speed, clouds]

    trace = go.Scattermapbox(
        lat=loc_lat,
        lon=loc_lon,
        mode='markers',
        marker=dict(
            size=15,
            color='magenta'
        ),
        text=curated_location,
        hoverinfo='text',
        showlegend=False
    )
    layout = go.Layout(
        height=500,
        width=950,
        margin=dict(l=0, t=0, r=0, b=0),
        mapbox_style='stamen-terrain',
        mapbox=dict(
            center=dict(
                lat=loc_lat[0],
                lon=loc_lon[0]
            ),
            zoom=5
        )
    )
    fig = go.Figure(data=[trace], layout=layout)

    map_result = html.Div([
        dcc.Graph(id='map-output', figure=fig)
    ], style={'paddingLeft' : 30})
    table_content = html.Div([
        dt.DataTable(
            id='table',
            columns=[{'name' : i, 'id' : i} for i in df.columns],
            data=df.to_dict('records')
        )
    ], style={'paddingRight' : 30})
    out_result = html.Div([
        html.Div([
            map_result
        ], className='eight columns'),
        html.Div([
            table_content
        ], className='four columns')
    ], className='row', style={'marginTop' : 50})

    return out_result




if __name__ == '__main__':
    app.run_server(debug=True)