import json
import pandas as pd
import os
import urllib.request

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

def load_catchments(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/catchments.geojson"
    )

    path = ensure_file(path, url)
    with open(path, encoding="utf-8") as f:
        geojson = json.load(f)


    return {
        f["properties"]["id"]: f
        for f in geojson["features"]
    }

def load_lakes(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/lakes.geojson"
    )

    path = ensure_file(path, url)

    with open(path, encoding="utf-8") as f:
        return json.load(f)
    

def load_lake_lookup(path):
    url = (
        "https://huggingface.co/datasets/mfth/ferro-dashboard/"
        "resolve/main/lakes.geojson"
    )

    path = ensure_file(path, url)

    with open(path, encoding="utf-8") as f:
        geojson = json.load(f)

    return {
        feature["properties"]["id"]: feature 
        for feature in geojson["features"]
    }

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
