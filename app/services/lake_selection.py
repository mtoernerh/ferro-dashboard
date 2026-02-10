# Import
from shapely.geometry import shape
from shapely.ops import transform

def find_lake_feature(triggered_id, click_data, selected_id, lakes_lookup):

    if triggered_id == "lake-selector" and selected_id:
        return lakes_lookup.get(triggered_id)

    if triggered_id == "lakes" and click_data:
        props = click_data.get("properties", {})
        lake_id = props.get("id") or props.get("id_str")

        return lakes_lookup.get(lake_id)

    return None

def compute_lake_metrics(lake_feature, catchment_by_id, crs):

    lake_id = lake_feature["properties"].get("id")
    lake_name = lake_feature["properties"].get("Name", "Unknown Lake")
    lake_geom = shape(lake_feature["geometry"])
    lake_centroid = lake_geom.centroid
    lake_area = transform(crs, lake_geom).area / 1e6

    catchment_feature = catchment_by_id.get(lake_id)

    if catchment_feature:
        catchment_geom = shape(catchment_feature["geometry"])
        catchment_area = transform(crs, catchment_geom).area / 1e6
    else:
        catchment_area = None

    return lake_id, lake_name, lake_centroid, lake_area, catchment_feature, catchment_area

def build_viewport(catchment_feature):

    if not catchment_feature:
        return None

    catchment_geom = shape(catchment_feature["geometry"])

    minx, miny, maxx, maxy = catchment_geom.bounds

    # Leaflet bounds are [[south, west], [north, east]]
    bounds = [
        [miny, minx],
        [maxy, maxx]
    ]

    return {"bounds": bounds, "transition": "flyToBounds"}

