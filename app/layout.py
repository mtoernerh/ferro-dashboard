
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
from app.components.map import create_map
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

        # --- 2. Unified Header (Logo + Dropdown + Button) ---
        html.Div([
            create_header(),
            create_dropdown(),
            create_legend_button()

        ], style={
            "display": "flex", 
            "alignItems": "center", 
            "justifyContent": "space-between", # Distributes items across the bar
            "padding": "0px 20px", 
            "flex": "0 0 auto",               # Fixed height based on content
            "borderBottom": "1px solid #333", # Subtle separator line
            "backgroundColor": "#121212"
        }),

        # --- 3. Main Content Area (Map) ---
        html.Div([
            create_map(),
            create_info_button(),
            create_legend()
        ], style={"flex": "1", "position": "relative", "overflow": "hidden"}), 

        # --- 4. Footer ---
        create_footer()

    ], style={
        "backgroundColor": "#121212", 
        "height": "100vh", 
        "width": "100%",          # Changed from 100vw to 100% to fix horizontal scroll
        "display": "flex", 
        "flexDirection": "column",
        "overflow": "hidden",      # Prevents scrollbars on the main window
        "padding": "0",
    })
    return layout