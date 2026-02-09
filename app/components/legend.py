from dash import html

def create_legend_button():
    return html.Button("Show Legend", id="legend-toggle", n_clicks=0,
                    style={"whiteSpace": "nowrap", "padding": "5px 15px", "cursor": "pointer", "width": "170px"})

def create_legend():
    return html.Div(
            id="legend",
            children=[
                html.H4("Legend", style={"marginBottom": "10px", "color": "white", "marginTop": "0"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#3388ff", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Lakes", style={"color": "white"})
                ], style={"marginBottom": "5px"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#33ff88", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Catchments", style={"color": "white"})
                ])
            ],
            style={
                "backgroundColor": "rgba(34, 34, 34, 0.9)", # Slightly transparent background
                "padding": "15px", 
                "borderRadius": "8px",
                "position": "absolute", 
                "top": "20px",    # 20px from the top of the MAP (not the screen)
                "right": "20px", 
                "zIndex": "1000",
                "display": "none", 
                "boxShadow": "0 0 10px rgba(0,0,0,0.5)"
            }
        )