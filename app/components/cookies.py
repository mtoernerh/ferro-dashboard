from dash import dcc, html

def create_cookie_store():
    return dcc.Store(id="cookie-store", storage_type="local")

def create_cookie_banner():
    return html.Div(
        id="cookie-banner",
        className="cookie-banner",
        children=[
            html.P(
                "We use cookies to improve your experience. By using this dashboard, you agree to our policy.",
                className="cookie-text"
            ),
            html.Button(
                "Accept",
                id="accept-cookies-btn",
                n_clicks=0,
                className="cookie-accept-btn"
            )
        ]
    )