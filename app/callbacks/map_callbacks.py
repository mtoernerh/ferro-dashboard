from dash import Output, Input, no_update, ctx
import dash_leaflet as dl
from pyproj import Transformer

from app.services.lake_selection import (
    find_lake_feature,
    compute_lake_metrics,
    build_viewport,
)
from app.components.popup import build_popup
from app.services.figures import generate_lake_sunburst
from app.services.app_data import get_app_data

def register_map_callbacks(app):

    @app.callback(
        Output("selected-catchment", "children"),
        Output("map", "viewport"),
        Input("lakes", "clickData"),
        Input("lake-selector", "value"),
        prevent_initial_call=True,
    )
    def update_on_click_or_dropdown(click_data, selected_id):
        project = Transformer.from_crs("EPSG:4326", "EPSG:25832", always_xy=True).transform
        data = get_app_data()

        triggered = ctx.triggered_id

        lake_feature = find_lake_feature(
            triggered,
            click_data,
            selected_id,
            data["lakes_geojson"],
        )

        if not lake_feature:
            return no_update, no_update

        (
            lake_id,
            lake_name,
            lake_centroid,
            lake_area,
            catchment_feature,
            catchment_area,
        ) = compute_lake_metrics(lake_feature, data["catchment_by_id"], project)

        # ---- dataframe lookups ----
        attributes_sel_df = data["attributes_df"][data["attributes_df"]["ID"] == lake_id].iloc[0]
        classes_sel_dict = (
            data["classes_df"][data["classes_df"]["ID"] == lake_id]
            .iloc[0]
            .drop("ID")
            .to_dict()
        )

        fig = generate_lake_sunburst(attributes_sel_df, classes_sel_dict)

        map_layers = [build_popup(lake_id, lake_name, lake_area, catchment_area, lake_centroid, fig)]

        if catchment_feature:
            map_layers.append(
                dl.GeoJSON(
                    data={
                        "type": "FeatureCollection",
                        "features": [catchment_feature],
                    },
                    options={"style": {"color": "green", "fillOpacity": 0.3}},
                )
            )

        viewport = build_viewport(catchment_feature)

        return map_layers, viewport
