from dash import Dash, dcc, html

def create_cookie_store():
    return dcc.Store(id="cookie-store", storage_type="local")


def create_cookie_banner():
    cookie_banner = html.Div(
        id="cookie-banner",
        children=[
            html.P("We use cookies to improve your experience. By using this dashboard, you agree to our policy.", 
                style={"margin": "0 10px 0 0", "color": "white"}),
            html.Button("Accept", id="accept-cookies-btn", n_clicks=0, 
                        style={"backgroundColor": "#3388ff", "color": "white", "border": "none", "padding": "5px 15px", "borderRadius": "4px", "cursor": "pointer"})
        ],
        style={
            "position": "fixed", "bottom": "0", "left": "0", "width": "100%",
            "backgroundColor": "#1a1a1a", "padding": "15px", "zIndex": "3000",
            "display": "flex", "justifyContent": "center", "alignItems": "center",
            "borderTop": "1px solid #333", "boxShadow": "0 -2px 10px rgba(0,0,0,0.5)", "overflow": "hidden",
        }
    )
    return cookie_banner