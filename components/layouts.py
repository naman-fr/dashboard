from dash import dcc, html
import dash_bootstrap_components as dbc
import json
import os

def get_layout():
    """
    Create the main layout with Bootstrap-based tabs.
    """
    # Load settings
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    with open(config_path) as f:
        settings = json.load(f)
    
    # Define tabs for Real-Time Data and Forecasting
    tabs = dbc.Tabs([
        dbc.Tab(label="Real-Time Analysis", tab_id="realtime"),
        dbc.Tab(label="Forecasting", tab_id="forecast")
    ], id="tabs", active_tab="realtime")
    
    layout = dbc.Container([
        html.H1(settings.get("app_title", "Real-Time Data Dashboard"), className="text-center my-4"),
        tabs,
        html.Div(id="tab-content", className="p-4")
    ], fluid=True)
    
    return layout
