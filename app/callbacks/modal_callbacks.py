from dash import Output, Input, no_update, ctx
#from app.styles import modal_style  # wherever you define it
#from .utils import compute_modal_style  # optional

def compute_modal_style(trigger_id, display_open="flex"):
    if trigger_id is None:
        return no_update
    if trigger_id.startswith("open"):
        return {"display": display_open}
    if trigger_id.startswith("close"):
        return {"display": "none"}
    return no_update

def register_modal_callbacks(app):
    def _register_modal(container_id, open_id, close_id):
        @app.callback(
            Output(container_id, "style"),
            Input(open_id, "n_clicks"),
            Input(close_id, "n_clicks"),
            prevent_initial_call=True,
        )
        def toggle_modal(_, __):
            return compute_modal_style(ctx.triggered_id)

    _register_modal("modal-imprint-container", "open-imprint", "close-imprint")
    _register_modal("modal-privacy-container", "open-privacy", "close-privacy")
    _register_modal("modal-info-container",    "open-info",    "close-info")