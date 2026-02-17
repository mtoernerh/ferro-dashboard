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
                    html.Div(style={"backgroundColor": "#b3b3b3", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Catchments", style={"color": "white"})
                ], style={"marginBottom": "5px"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#00B0F0", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                   html.Span("Lake Type 1 – Relatively low eutrophication risk")
                ], style={"marginBottom": "5px"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#92D050", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Lake Type 2 – Moderate eutrophication risk")
                ], style={"marginBottom": "5px"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#FFFF00", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Lake Type 3 – Risk strongly dependent on drainage basin changes")
                ], style={"marginBottom": "5px"}),
                html.Div([
                    html.Div(style={"backgroundColor": "#FF0000", "width": "20px", "height": "20px", "display": "inline-block", "marginRight": "10px"}),
                    html.Span("Lake Type 4 – High eutrophication risk")
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