import json
import pandas as pd
import os
import urllib.request
import fiona
from functools import lru_cache

def ensure_file(path, url):
    """
    Ensure file exists locally.
    If not, download from URL and save to path.
    """
    if os.path.exists(path):
        return path

    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        raise RuntimeError(f"Failed to download {url}: {e}")

    return path

@lru_cache(maxsize=1)
def build_catchment_index(path):
    """Build {id: fiona_integer_index} once. Stores only ints, not geometries."""
    index = {}
    with fiona.open(str(path)) as src:
        for i, feature in enumerate(src):
            index[feature["properties"]["id"]] = i
    return index

#def load_catchments(path):
#    url = (
#        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
#        "resolve/main/catchments.geojson"
#    )
#
#    path = ensure_file(path, url)
#    with open(path, encoding="utf-8") as f:
#        geojson = json.load(f)
#
#
#    return {
#        f["properties"]["id"]: f
#        for f in geojson["features"]
#    }

#@lru_cache(maxsize=64)
def load_catchment_by_id(path, lake_id):
    index = build_catchment_index(path)
    idx = index.get(lake_id)
    if idx is None:
        return None
    with fiona.open(str(path)) as src:
        feature = src[idx]
        return {
            "type": "Feature",
            "geometry": dict(feature["geometry"]),
            "properties": dict(feature["properties"]),
        }

def load_lakes(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/lakes.geojson"
    )

    path = ensure_file(path, url)

    with open(path, encoding="utf-8") as f:
        return json.load(f)
    
def get_catchment(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/catchments.geojson"
    )

    path = ensure_file(path, url)
    
#def load_lake_lookup(path):
#    url = (
#        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
#        "resolve/main/lakes.geojson"
#    )
#
#    path = ensure_file(path, url)
#
#    with open(path, encoding="utf-8") as f:
#        geojson = json.load(f)
#
#    return {
#        feature["properties"]["id_str"]: feature 
#        for feature in geojson["features"]
#    }
def load_metrics(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/lake_metrics_v2.3.parquet"
    )

    path = ensure_file(path, url)
    return pd.read_parquet(path)

def load_attributes(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/attributes_v2.3.parquet"
    )

    path = ensure_file(path, url)
    return pd.read_parquet(path)

def load_classes(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/classes_v2.3.parquet"
    )

    path = ensure_file(path, url)
    return pd.read_parquet(path)
