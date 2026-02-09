# -*- coding: utf-8 -*-
from dash import html

def create_info_button():
    return html.Img(
            src="/assets/info.svg",
            id="open-info",
            n_clicks=0,
            style={
                "position": "absolute",
                "bottom": "20px",      # Distance from bottom edge of map
                "left": "20px",        # Distance from left edge of map
                "zIndex": "1001",      # Above the map
                "height": "35px",      # Adjust size as needed
                "cursor": "pointer",
                "filter": "invert(1)"  # Use this if your SVG is black but you want it white for dark mode
            }
        )