import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = Path(
    os.getenv("DASH_DATA_DIR", BASE_DIR / "data")
)

GEOJSON_DIR = DATA_DIR / "geojson"
TABLES_DIR = DATA_DIR / "tables"
