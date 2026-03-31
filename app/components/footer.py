from dash import html

def create_footer():
    eu_funding_text = (
        "FERRO receives funding from the European Union's Horizon Europe research "
        "and innovation programme under grant agreement No. 101157743. "
        "Views and opinions expressed are those of the author(s) only and do not "
        "necessarily reflect those of the European Union or the European Climate, "
        "Infrastructure and Environment Executive Agency (CINEA). "
        "Neither the EU nor CINEA can be held responsible for them."
    )
    return html.Div([
        html.Div([
            # -------- LEFT: EU box --------
            html.Div([
                html.Img(src="/assets/eu_logo.png", className="footer-eu-logo"),
                html.Div(eu_funding_text, className="footer-eu-text")
            ], className="footer-eu"),

            # -------- CENTER: links --------
            html.Div([
                html.Span("© 2026 Ferro Viewer", style={"marginRight": "20px"}),
                html.A("Imprint", id="open-imprint", n_clicks=0,
                       style={"cursor": "pointer", "marginRight": "15px", "textDecoration": "underline"}),
                html.A("Privacy Policy", id="open-privacy", n_clicks=0,
                       style={"cursor": "pointer", "textDecoration": "underline"}),
            ], className="footer-links"),

            # -------- RIGHT: spacer (desktop only) --------
            html.Div(className="footer-spacer")
        ], className="footer-inner")
    ], className="footer-bar")
