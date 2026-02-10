from dash import Output, Input, State, no_update, html
from app.components.map import create_map

def register_cookie_callback(app):

    @app.callback(
        Output("cookie-banner", "style"),
        Output("cookie-store", "data"),
        Input("accept-cookies-btn", "n_clicks"),
        State("cookie-store", "data"),
        State("cookie-banner", "style"),
        
    )
    def handle_cookie_consent(n_clicks, stored_data, current_style):

        # Already accepted in previous session
        if stored_data and stored_data.get("accepted"):
            return {**current_style, "display": "none"}, stored_data

        # User just accepted
        if n_clicks:
            return {**current_style, "display": "none"}, {"accepted": True}

        # Nothing to do
        return no_update, no_update

def register_map_content_callback(app):
    @app.callback(
        Output("map-content-container", "children"),
        Input("cookie-store", "data")
    )
    def update_map_visibility(cookie_data):
        # Case 1: Cookies are accepted
        if cookie_data and cookie_data.get("accepted"):
            # We assume create_map() returns a dl.Map or dcc.Graph component
            return create_map()
        
        # Case 2: Cookies NOT accepted (Initial Load)
        # Return a placeholder message instead of the map
        return html.Div(
            [
                html.H3("Map Disabled", style={"color": "#888"}),
                html.P("Please accept cookies to load OpenStreetMap data.", style={"color": "#666"})
            ],
            style={
                "height": "100%",
                "width": "100%",
                "display": "flex",
                "flexDirection": "column",
                "alignItems": "center",
                "justifyContent": "center",
                "backgroundColor": "#000" # Match your dark theme
            }
        )