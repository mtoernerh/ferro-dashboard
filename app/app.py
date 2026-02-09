from dash import Dash
from app.layout import layout
from app.callbacks import register_callbacks


def create_app():
    app = Dash(
        __name__,
        suppress_callback_exceptions=True,
    )

    app.layout = layout()
    register_callbacks(app)

    return app