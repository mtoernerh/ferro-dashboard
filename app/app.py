from app.custom_dash import CustomDash
from app.layout import layout
from app.callbacks import register_callbacks


def create_app():
    app = CustomDash(
        __name__,
        suppress_callback_exceptions=True,
        title="Lake Risk",
    )
    app.layout = layout()
    register_callbacks(app)

    return app