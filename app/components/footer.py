from dash import html

def create_footer():
    return html.Div([
        html.Span("© 2026 Ferro Dashboard", style={"marginRight": "20px"}),
        html.A("Imprint", id="open-imprint", n_clicks=0, style={"cursor": "pointer", "marginRight": "15px", "textDecoration": "underline"}),
        html.A("Privacy Policy", id="open-privacy", n_clicks=0, style={"cursor": "pointer", "textDecoration": "underline"}),
    ], style={
        "textAlign": "center", "color": "#888", "padding": "10px 12px", 
        "fontSize": "13px", "backgroundColor": "#121212", "borderTop": "1px solid #333",
        "flex": "0 1 auto"
    })