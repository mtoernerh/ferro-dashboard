from dash import dcc, html
import dash_leaflet as dl

def build_popup(lake_id, lake_name, lake_area, catchment_area, lake_centroid, fig):
    legend_item = lambda color, label: html.Div([
        html.Span(style={
            "display": "inline-block", "width": "14px", "height": "14px",
            "backgroundColor": color, "marginRight": "8px", "flexShrink": "0",
            "border": "0.5px solid #ccc"
        }),
        html.Span(label)
    ], style={"marginBottom": "3px", "display": "flex", "alignItems": "center"})

    scale_labels = ["1 – Very low", "2 – Low", "3 – Moderate", "4 – High"]
    brown_colors = ["#fff2cc", "#ffd966", "#bf9000", "#7f6000"]
    blue_colors  = ["#dae3f3", "#8faadc", "#2f5597", "#203864"]

    def mini_legend(title, colors, labels):
        return html.Div([
            html.Div(title, style={
                "fontWeight": "bold", "fontSize": "11px",
                "marginBottom": "4px", "color": "#444"
            }),
            *[legend_item(c, l) for c, l in zip(colors, labels)]
        ], style={"flex": "1", "minWidth": "0"})

    return dl.Popup(
        children=[
            html.Div([
                html.H4(lake_name, style={"marginTop": "0", "fontSize": "20px"}),
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False, "responsive": True},
                    style={"width": "100%", "height": "260px", "margin": "10px 0"}
                ),

                # --- Eutrophication risk legend (unchanged) ---
                html.Div([
                    legend_item("#00B0F0", "Type 1 – Relatively low eutrophication risk"),
                    legend_item("#92D050", "Type 2 – Moderate eutrophication risk"),
                    legend_item("#FFFF00", "Type 3 – Risk strongly dependent on drainage basin changes"),
                    legend_item("#FF0000", "Type 4 – High eutrophication risk"),
                ], style={"fontSize": "12px", "marginBottom": "8px"}),

                # --- Two-column scales (side by side, no extra height) ---
                html.Div([
                    mini_legend("🟤 Nutrient load potential", brown_colors, scale_labels),
                    html.Div(style={"width": "12px"}),  # spacer
                    mini_legend("🔵 Inherent lake sensitivity", blue_colors, scale_labels),
                ], style={
                    "display": "flex", "flexDirection": "row",
                    "fontSize": "11px", "marginBottom": "8px"
                }),

                html.Hr(style={"border": "0.5px solid #eee"}),
                html.P([
                    html.B("ID: "), f"{lake_id}", html.Br(),
                    html.B("Lake Area: "), f"{lake_area:.2f} km²", html.Br(),
                    html.B("Catchment: "), f"{catchment_area:.2f} km²" if catchment_area else "N/A", html.Br(),
                    html.Small(f"Coords: {lake_centroid[1]:.3f}, {lake_centroid[0]:.3f}",
                               style={"color": "gray"})
                ])
            ], className="popup-content")
        ],
        position=[lake_centroid[1], lake_centroid[0]],
        maxWidth=500,
        autoClose=False,
        autoPan=True,
    )