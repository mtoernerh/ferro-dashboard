from dash import dcc, html
from app.services.app_data import get_app_data

def create_dropdown():
    data = get_app_data()
    return html.Div([
        dcc.Dropdown(
            id="lake-selector",
            options=[
                {
                    "label": f["properties"]["Name"],
                    "value": f["properties"]["id_str"]
                }
                for f in data["lakes_lookup"].values() 
            ],
            placeholder="Search for a lake...",
            style={"width": "100%", "color": "#ffffff"}
        )
    ], className="header-dropdown")
