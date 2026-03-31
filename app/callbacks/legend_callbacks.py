from dash import Input, Output

def register_legend_callback(app):
    @app.callback(
        Output("legend", "style"),
        Output("legend-toggle", "children"),
        Input("legend-toggle", "n_clicks"),
    )
    def toggle_legend(n_clicks):
        if n_clicks and n_clicks % 2 == 1:
            return {"display": "none"}, "Show Legend"
        return {"display": "block"}, "Hide Legend"