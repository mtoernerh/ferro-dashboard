import dash_leaflet as dl
from dash import html
from app.services.app_data import get_app_data

def create_map():
    data = get_app_data()
    lakes_layer = dl.GeoJSON(
            data= data["lakes_geojson"],
            id="lakes",
            zoomToBoundsOnClick=False,
            options={"style": {"color": "blue", "fillOpacity": 0.5}},
            hoverStyle={"weight": 2, "color": "cyan"},
            interactive=True
        )

    catchment_layer = dl.LayerGroup(id="selected-catchment")

    map_view = dl.Map(id = "map", center=[56, 10], trackResize = True, zoom=6, children=[
        dl.TileLayer(),
        lakes_layer,
        catchment_layer,
    ], style={'width': '105%', 'height': '100%', 'margin': "auto", "display": "block", "overflow": "hidden"})

    return html.Div(map_view, style={"height": "100%", "width": "105%", "position": "absolute", "top": "0", "left": "0", "zIndex": "0"})