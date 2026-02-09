from dash import html

def create_header():
    return html.Div([ 
            html.Img(src="/assets/ferro_logo.png", style={"height": "60px", "marginRight": "10px"}),
            html.H2("Dashboard", style={"color": "white", "margin": "0", "fontSize": "22px", "whiteSpace": "nowrap"})
        ], style={"display": "flex", "alignItems": "center", "marginRight": "20px"})