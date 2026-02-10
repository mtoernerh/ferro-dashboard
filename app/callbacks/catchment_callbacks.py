from dash import ctx, no_update, Input, Output
from pyproj import Transformer
import dash_leaflet as dl

from app.services.lake_selection import (
    compute_lake_metrics,
)
from app.components.popup import build_popup
from app.services.figures import generate_lake_sunburst
from app.services.app_data import get_app_data

def register_catchment_callbacks(app):

    @app.callback(
        Output("selected-catchment", "children", allow_duplicate=True),
        Input("catchments", "clickData"),
        prevent_initial_call=True,
    )
    def update_on_catchment_click(click_data):
        if not click_data:
            return no_update

        project = Transformer.from_crs(
            "EPSG:4326", "EPSG:25832", always_xy=True
        ).transform

        data = get_app_data()

        lake_id  = click_data["properties"]["id"]

        lake_feature = next(
            (
                f for f in  data["lakes_geojson"]["features"]
                if f.get("properties", {}).get("id") == lake_id
                ),
            None,
        )
        
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

        popup = build_popup(
            lake_id,
            lake_name,
            lake_area,
            catchment_area,
            lake_centroid,
            fig,
        )

        map_layers = [popup]

        map_layers.append(
                dl.GeoJSON(
                    id = "catchments",
                    data={
                        "type": "FeatureCollection",
                        "features": [catchment_feature],
                    },
                    options={"style": {"color": "green", "fillOpacity": 0.3}, "interactive": True},
                )
            )

        # IMPORTANT:
        # - Do NOT add GeoJSON
        # - Do NOT update viewport
        return map_layers
