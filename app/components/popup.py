from dash import dcc, html
import dash_leaflet as dl

def build_popup(lake_id, lake_name, lake_area, catchment_area, lake_centroid, fig):
    return dl.Popup(
            children=[
                html.Div([
                    html.H4(lake_name, style={"margin-top": "0", "font-size": "24px"}),

                    dcc.Graph(
                        figure=fig,
                        config={
                            "displayModeBar": False,
                            "responsive": True
                        },
                        style={
                            "width": "100%",
                            "height": "300px",
                            "margin": "10px 0"
                        }
                    ),

                    html.Hr(style={"border": "0.5px solid #eee"}),

                    html.P([
                        html.B("ID: "), f"{lake_id}", html.Br(),
                        html.B("Lake Area: "), f"{lake_area:.2f} km²", html.Br(),
                        html.B("Catchment: "), f"{catchment_area:.2f} km²" if catchment_area else "N/A", html.Br(),
                        html.Small(f"Coords: {lake_centroid.y:.3f}, {lake_centroid.x:.3f}", style={"color": "gray"})
                    ])
                ], style={"minWidth": "500px"})
            ],
            position=[lake_centroid.y, lake_centroid.x],
            maxWidth=500,
            autoClose=False,
            autoPan = True,
        )