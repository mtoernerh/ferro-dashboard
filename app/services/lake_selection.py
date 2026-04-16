from app.services.data_registry import load_catchment_by_id

def find_lake_feature(triggered_id, click_data, selected_id, lakes_lookup):

    if triggered_id == "lake-selector" and selected_id:
        return lakes_lookup.get(selected_id)

    if triggered_id == "lakes" and click_data:
        props = click_data.get("properties", {})
        lake_id = props.get("id_str")

        return lakes_lookup.get(lake_id)

    return None

def compute_lake_metrics(lake_feature, catchments_path, lake_metrics_df):
    lake_id   = lake_feature["properties"]["id_str"]
    lake_name = lake_feature["properties"].get("Name", "Unknown Lake")
    
    row = lake_metrics_df[lake_metrics_df["id_str"] == lake_id].iloc[0]
    
    lake_centroid   = (row["centroid_lon"], row["centroid_lat"])
    lake_area       = row["lake_area_km2"]
    catchment_area  = row["catch_area_km2"]   # NaN if no catchment
    bounds          = row["bounds"]            # pre-computed [[S,W],[N,E]]

    catchment_feature = load_catchment_by_id(catchments_path, lake_id)
    
    return lake_id, lake_name, lake_centroid, lake_area, catchment_feature, catchment_area, bounds

def build_viewport(bounds):
    if bounds is None:
        return None
    return {"bounds": bounds, "transition": "flyToBounds"}

