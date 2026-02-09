from dash import Output, Input, State, ctx
#from app.styles import modal_style  # wherever you define it
#from .utils import compute_modal_style  # optional

def compute_modal_style(trigger_id, current_style, display_open="flex"):
    base_style = current_style or {}
    
    if trigger_id is None:
        return base_style

    if trigger_id.startswith("open"):
        return {**base_style, "display": display_open}

    if trigger_id.startswith("close"):
        return {**base_style, "display": "none"}

    return base_style

def register_modal_callbacks(app):

    def _register_modal(container_id, open_id, close_id):

        @app.callback(
            Output(container_id, "style"),
            Input(open_id, "n_clicks"),
            Input(close_id, "n_clicks"),
            State(container_id, "style"),
            prevent_initial_call=True,
        )
        def toggle_modal(_, __, current_style):
            trigger_id = ctx.triggered_id
            return compute_modal_style(trigger_id, current_style)

    # Register all modals here
    _register_modal(
        container_id="modal-imprint-container",
        open_id="open-imprint",
        close_id="close-imprint",
    )

    _register_modal(
        container_id="modal-privacy-container",
        open_id="open-privacy",
        close_id="close-privacy",
    )

    _register_modal(
        container_id="modal-info-container",
        open_id="open-info",
        close_id="close-info",
    )