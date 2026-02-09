# Import
from dash import html, dcc
import os
from pathlib import Path
modal_style = {
    "position": "fixed", "zIndex": "2000", "top": "0", "left": "0",
    "width": "100%", "height": "100%", "backgroundColor": "rgba(0,0,0,0.8)",
    "display": "none", "justifyContent": "center", "alignItems": "center"
}

modal_content_style = {
    "backgroundColor": "#222", "padding": "20px", "borderRadius": "8px",
    "width": "60%", "maxWidth": "600px", "color": "white", "position": "relative",
    "border": "1px solid #444", "maxHeight": "80vh", "overflowY": "auto"
}

ASSETS_PATH = os.path.join(Path(os.path.dirname(__file__)).parent.absolute(), "assets")

def load_text_file(filename):
    """Load a text file from assets and return as list of paragraphs"""
    file_path = os.path.join(ASSETS_PATH, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Split into paragraphs by double newlines
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs


def load_text_file(filename):
    """Load a text file from assets and return as string"""
    file_path = os.path.join(ASSETS_PATH, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def create_info_modal():
    paragraphs = load_text_file("info_text.txt") 
    info_modal = html.Div(
        id="modal-info-container",
        style=modal_style, 
        children=[
            html.Div(style=modal_content_style, children=[
                html.Button("X", id="close-info", n_clicks=0, style={"float": "right", "background": "none", "border": "none", "color": "white", "fontSize": "20px", "cursor": "pointer"}),
                html.H3("Project Information"),
                html.P(paragraphs),

            ])
        ]
    )
    return info_modal

def create_footer():
    footer = html.Div([
        html.Span("© 2024 Ferro Dashboard", style={"marginRight": "20px"}),
        html.A("Imprint", id="open-imprint", n_clicks=0, style={"cursor": "pointer", "marginRight": "15px", "textDecoration": "underline"}),
        html.A("Privacy Policy", id="open-privacy", n_clicks=0, style={"cursor": "pointer", "textDecoration": "underline"}),
    ], style={
        "textAlign": "center", "color": "#888", "padding": "10px", 
        "fontSize": "12px", "marginTop": "auto" # Push to bottom if using flex column
    })
    return footer


def create_imprint_modal():
    paragraphs = load_text_file("imprint.txt")
    imprint_modal = html.Div(
        id="modal-imprint-container",
        style=modal_style,
        children=[
            html.Div(style=modal_content_style, children=[
                html.Button("X", id="close-imprint", n_clicks=0, style={"float": "right", "background": "none", "border": "none", "color": "white", "fontSize": "20px", "cursor": "pointer"}),
                dcc.Markdown(
                        paragraphs,
                        style={"whiteSpace": "pre-wrap", "color": "white"}  # preserves line breaks
                    ),
            ])
        ]
    )
    return imprint_modal

def create_privacy_modal():
    paragraphs = load_text_file("privacy_policy.txt")
    privacy_modal = html.Div(
        id="modal-privacy-container",
        style=modal_style,
        children=[
            html.Div(style=modal_content_style, children=[
                html.Button("X", id="close-privacy", n_clicks=0, style={"float": "right", "background": "none", "border": "none", "color": "white", "fontSize": "20px", "cursor": "pointer"}),
                dcc.Markdown(
                        paragraphs,
                        style={"whiteSpace": "pre-wrap", "color": "white"}  # preserves line breaks
                    ), 
            ])
        ]
    )
    return privacy_modal