
from dash import html
from app.components.cookies import create_cookie_store
from app.components.modals import (
    create_imprint_modal,
    create_privacy_modal,
    create_info_modal
)
from app.components.cookies import create_cookie_banner
from app.components.header import create_header
from app.components.dropdown import create_dropdown
from app.components.legend import create_legend_button, create_legend
from app.components.info_button import create_info_button
from app.components.footer import create_footer

def layout():
    layout = html.Div([
        # --- 1. Invisible Logic Components ---
        create_cookie_store(),
        create_imprint_modal(),
        create_privacy_modal(),
        create_info_modal(),
        create_cookie_banner(),

        # --- 2. Header Bar ---
        html.Div([
            create_header(),
            create_dropdown(),
            create_legend_button()
        ], className="header-bar"),

        # --- 3. Main Content Area (Map) ---
        html.Div([
            html.Div(
                id="map-content-container",
                style={
                    "height": "100%",
                    "width": "100%",
                    "position": "absolute",
                    "top": 0,
                    "left": 0
                }
            ),
            create_info_button(),
            create_legend()
        ], style={"flex": "1", "position": "relative", "overflow": "hidden"}),
        
        # --- 4. Footer ---
        create_footer()
        # --- 2. Unified Header (Logo + Dropdown + Button) ---

        ], style={
        "backgroundColor": "#121212",
        "height": "100vh",
        "width": "100%",
        "display": "flex",
        "flexDirection": "column",
        "overflow": "hidden",
        "padding": "0",
    })
    return layout