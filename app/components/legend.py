from dash import html

def create_legend_button():
    return html.Button(
        "Hide Legend",
        id="legend-toggle",
        n_clicks=0,
        className="legend-toggle-btn"
    )

def create_legend():
    legend_item = lambda color, label: html.Div([
        html.Div(style={
            "backgroundColor": color,
            "width": "10px", "height": "10px",
            "display": "inline-block", "marginRight": "8px",
            "flexShrink": "0"
        }),
        html.Span(label, style={"color": "white", "fontSize": "10px"})
    ], style={"marginBottom": "4px", "display": "flex", "alignItems": "center"})

    return html.Div(
        id="legend",
        className="legend-container",
        children=[
            html.H4("Legend", style={"marginBottom": "8px", "color": "white", "marginTop": "0", "fontSize": "10px"}),
            legend_item("#b3b3b3", "Catchments"),
            legend_item("#00B0F0", "Lake Type 1 – Relatively low eutrophication risk"),
            legend_item("#92D050", "Lake Type 2 – Moderate eutrophication risk"),
            legend_item("#FFFF00", "Lake Type 3 – Risk strongly dependent on drainage basin changes"),
            legend_item("#FF0000", "Lake Type 4 – High eutrophication risk"),
        ]
    )