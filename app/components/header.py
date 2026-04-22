from dash import html

def create_header():
    return html.Div([
        html.Img(src="/assets/ferro_logo.png", className="header-logo"),
        html.H2("Lake Sensitivity to Eutrophication", className="header-title")
    ], className="header-brand")