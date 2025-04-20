import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import json
import os

from components.layouts import get_layout
from components.figures import build_line_chart
from data.fetching import fetch_data
from data.processing import process_data
from models.forecasting import forecast_data

# Create Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set the app layout
app.layout = get_layout()

# Callback to render tab content
@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab")]
)
def render_tab_content(active_tab):
    # Load configuration
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'settings.json')
    with open(config_path) as f:
        settings = json.load(f)
    
    if active_tab == "realtime":
        # Real-time Analysis: graph with Interval update
        return html.Div([
            dcc.Graph(id='live-update-graph'),
            dcc.Interval(
                id='graph-update',
                interval=settings.get("update_interval", 10000),
                n_intervals=0
            )
        ])
    elif active_tab == "forecast":
        # Forecasting Tab: graph without interval and with a slider to adjust forecast horizon.
        return html.Div([
            html.H4("Forecast Horizon"),
            dcc.Slider(
                id='forecast-horizon-slider',
                min=1,
                max=20,
                step=1,
                value=settings.get("forecast_horizon", 5),
                marks={i: str(i) for i in range(1, 21)}
            ),
            dcc.Graph(id='forecast-graph')
        ])
    else:
        return html.Div("No content available.")

# Callback for Real-Time Graph updating
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_realtime_graph(n):
    df = fetch_data()
    df = process_data(df)
    # Build the real-time figure without forecast overlay
    fig = build_line_chart(df)
    return fig

# Callback for Forecast Graph (runs on user adjusting forecast horizon)
@app.callback(
    Output('forecast-graph', 'figure'),
    [Input('forecast-horizon-slider', 'value')]
)
def update_forecast_graph(horizon):
    # Get the latest data
    df = fetch_data()
    df = process_data(df)
    # Forecast future values
    forecast_df = forecast_data(df, horizon=horizon)
    # Build the graph with forecast overlay
    fig = build_line_chart(df, forecast_df=forecast_df)
    return fig

if __name__ == '__main__':
    # Load settings
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'settings.json')
    with open(config_path) as f:
        settings = json.load(f)
    
    app.run(debug=settings.get("debug", False), port=settings.get("default_port", 8050))
