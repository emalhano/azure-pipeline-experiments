import dash_bootstrap_components as dbc
import dash
import yaml
from dash import dcc, html, Input, Output

from utils.functions import create_time_series_plot

# Sample data for demonstration
with open('utils/config.yaml', 'r') as file:
    app_config = yaml.safe_load(file)['App config']


# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Layout of the dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(
                "Experimental FastF1 App",
                className="text-center mb-4",
                style={
                    "color": "#e10600",  # F1 red color
                    "fontWeight": "bold",
                    "textShadow": "2px 2px 4px rgba(0,0,0,0.3)",
                    "marginTop": "20px",
                    "fontFamily": "'Arial Black', sans-serif"
                }
            )
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='year-dropdown',
                options=app_config['years'],
                value=app_config['years'][-1],
                placeholder="Select Year"
            )
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='track-dropdown',
                options=app_config['tracks'],
                placeholder="Select Track"
            )
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='session-dropdown',
                options=app_config['sessions'],
                placeholder="Select Session"
            )
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id='driver-dropdown',
                options=app_config['drivers'],
                placeholder="Select Driver"
            )
        ], width=2),
    ], className="mb-4"),  # Add margin-bottom for spacing
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='plot-area')
        ], width=12)
    ])
], fluid=True)  # Use fluid=True for responsive layout




@app.callback(
    Output('plot-area', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('track-dropdown', 'value'),
     Input('session-dropdown', 'value'),
     Input('driver-dropdown', 'value')]
)
def update_plot(track, year, session, driver):

    return create_time_series_plot(track, year, session, driver)




# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)