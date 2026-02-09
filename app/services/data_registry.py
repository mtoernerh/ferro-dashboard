import json
import pandas as pd

def load_catchments(path):
    with open(path, encoding="utf-8") as f:
        geojson = json.load(f)

    return {
        f["properties"]["id"]: f
        for f in geojson["features"]
    }

def load_lakes(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def load_attributes(path):
    return pd.read_parquet(path)

def load_classes(path):
    return pd.read_parquet(path)
