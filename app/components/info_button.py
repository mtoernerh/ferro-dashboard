# -*- coding: utf-8 -*-
from dash import html

def create_info_button():
    return html.Img(
        src="/assets/info.svg",
        id="open-info",
        n_clicks=0,
        className="info-button",
        style={"filter": "invert(1)"}
    )