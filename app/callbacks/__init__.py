def register_callbacks(app):
    from .cookie_callbacks import register_cookie_callback
    from .legend_callbacks import register_legend_callback
    from .map_callbacks import register_map_callbacks
    from .modal_callbacks import register_modal_callbacks

    register_cookie_callback(app)
    register_legend_callback(app)
    register_map_callbacks(app)
    register_modal_callbacks(app)