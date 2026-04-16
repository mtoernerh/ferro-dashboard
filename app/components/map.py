import dash_leaflet as dl
from dash import html
from dash_extensions.javascript import Namespace

ns = Namespace("dashExtensions", "my_namespace")
style_handle = ns("lake_style")

def create_map():
    classes = [1, 2, 3, 4]
    colorscale = ["#00B0F0", "#92D050", "#FFFF00", "#FF0000"]
    style = dict(weight=2, opacity=1, color="white", dashArray="3", fillOpacity=0.7)

    lakes_layer = dl.GeoJSON(
        url="/assets/lakes.geojson",
        id="lakes",
        style=style_handle,
        zoomToBoundsOnClick=False,
        hoverStyle=dict(weight=5, color="#666", dashArray=""),
        hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp="Lake Type"),
        interactive=True
    )
    
    catchment_layer = dl.LayerGroup(id="selected-catchment")

    map_view = dl.Map(
        id="map",
        center=[56, 10],
        trackResize=True,
        zoom=6,
        children=[
            dl.TileLayer(
                url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png",
                subdomains=["a", "b", "c", "d"],
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                            'contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
            ),
            lakes_layer,
            catchment_layer,
        ],
        style={"width": "100%", "height": "100%"}
    )
    return html.Div(
        map_view,
        style={
            "height": "100%", "width": "100%",
            "position": "absolute", "top": "0", "left": "0", "zIndex": "0"
        }
    )