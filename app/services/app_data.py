from functools import lru_cache
from config import GEOJSON_DIR, TABLES_DIR, ASSET_DIR
from app.services.data_registry import (
 #   load_catchments,
    build_catchment_index,
    get_catchment,
    load_lakes,
    load_attributes,
    load_classes,
    load_metrics
)

@lru_cache(maxsize=4)
def get_app_data():
    """
    Loads and stores all static datasets once per process.
    """
    lakes_geojson = load_lakes(ASSET_DIR / "lakes.geojson")
    catchments_path = GEOJSON_DIR / "catchments.geojson"
    get_catchment(catchments_path)
    build_catchment_index(catchments_path) 
    return {
        "catchments_path":  GEOJSON_DIR / "catchments.geojson",
        "attributes_df":    load_attributes(TABLES_DIR / "attributes_v2.3.parquet"),
        "classes_df":       load_classes(TABLES_DIR / "classes_v2.3.parquet"),
        "lakes_lookup":     {f["properties"]["id_str"]: f for f in lakes_geojson["features"]},
        "lake_metrics":     load_metrics(TABLES_DIR / "lake_metrics_v2.3.parquet"),  # new
    }
