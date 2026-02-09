from dash import Input, Output, State

def register_legend_callback(app):
    @app.callback(
        Output("legend", "style"),
        Output("legend-toggle", "children"),
        Input("legend-toggle", "n_clicks"),
        State("legend", "style"),
    )
    def toggle_legend(n_clicks, current_style):
        if n_clicks % 2 == 1:
            new_style = current_style.copy()
            new_style["display"] = "block"
            return new_style, "Hide Legend"
        else:
            new_style = current_style.copy()
            new_style["display"] = "none"
            return new_style, "Show Legend"