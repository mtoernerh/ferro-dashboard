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
                        "value": f["properties"]["id"]
                    }
                    for f in data["lakes_geojson"]["features"]
                ],
                placeholder="Search for a lake...",
                # Note: 'color': '#000' ensures text is visible inside the white dropdown box
                style={"width": "100%", "color": "#ffffff"} 
            )
        ], style={"flex": "1", "maxWidth": "500px", "margin": "0 20px"})

