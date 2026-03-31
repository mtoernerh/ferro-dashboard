from dash import dcc, html
import dash_leaflet as dl

def build_popup(lake_id, lake_name, lake_area, catchment_area, lake_centroid, fig):
    legend_item = lambda color, label: html.Div([
        html.Span(style={
            "display": "inline-block", "width": "14px", "height": "14px",
            "backgroundColor": color, "marginRight": "8px", "flexShrink": "0"
        }),
        html.Span(label)
    ], style={"marginBottom": "4px", "display": "flex", "alignItems": "center"})

    return dl.Popup(
        children=[
            html.Div([
                html.H4(lake_name, style={"marginTop": "0", "fontSize": "20px"}),
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False, "responsive": True},
                    style={"width": "100%", "height": "260px", "margin": "10px 0"}
                ),
                html.Div([
                    legend_item("#00B0F0", "Type 1 – Relatively low eutrophication risk"),
                    legend_item("#92D050", "Type 2 – Moderate eutrophication risk"),
                    legend_item("#FFFF00", "Type 3 – Risk strongly dependent on drainage basin changes"),
                    legend_item("#FF0000", "Type 4 – High eutrophication risk"),
                ], style={"fontSize": "12px", "marginBottom": "10px"}),
                html.Hr(style={"border": "0.5px solid #eee"}),
                html.P([
                    html.B("ID: "), f"{lake_id}", html.Br(),
                    html.B("Lake Area: "), f"{lake_area:.2f} km²", html.Br(),
                    html.B("Catchment: "), f"{catchment_area:.2f} km²" if catchment_area else "N/A", html.Br(),
                    html.Small(f"Coords: {lake_centroid.y:.3f}, {lake_centroid.x:.3f}",
                               style={"color": "gray"})
                ])
            ], className="popup-content")
        ],
        position=[lake_centroid.y, lake_centroid.x],
        maxWidth=500,
        autoClose=False,
        autoPan=True,
    )