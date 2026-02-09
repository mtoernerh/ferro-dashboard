from dash import Output, Input, State, no_update

def register_cookie_callback(app):

    @app.callback(
        Output("cookie-banner", "style"),
        Output("cookie-store", "data"),
        Input("accept-cookies-btn", "n_clicks"),
        State("cookie-store", "data"),
        State("cookie-banner", "style"),
        prevent_initial_call=True,
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
