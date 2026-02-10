from functools import lru_cache
from config import GEOJSON_DIR, TABLES_DIR
from app.services.data_registry import (
    load_catchments,
    load_lakes,
    load_attributes,
    load_classes,
    load_lake_lookup
)

@lru_cache(maxsize=4)
def get_app_data():
    """
    Loads and stores all static datasets once per process.
    """
    return {
        "lakes_geojson": load_lakes(GEOJSON_DIR / "lakes.geojson"),
        "catchment_by_id": load_catchments(GEOJSON_DIR / "catchments.geojson"),
        "attributes_df": load_attributes(TABLES_DIR / "attributes_v2.3.parquet"),
        "classes_df": load_classes(TABLES_DIR / "classes_v2.3.parquet"),
        "lakes_lookup": load_lake_lookup(GEOJSON_DIR / "lakes.geojson"),
    }
