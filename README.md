# FERRO Dashboard

Dashboard for the **FERRO** project, providing an overview of existing lake and associated catchment along with classifcation of
eutrophication risk. 

## Requirements

A Python environment with the following packages:

- `dash`
- `dash-leaflet`
- `pandas`
- `geopandas`
- `shapely`
- `plotly`
- `pyproj`  

Clone the repository and create the environment using the provided environment.yml file:
```bash
git clone <repo-url>
cd ferro-dashboard
conda env create -f environment.yml
conda activate ferro-dashboard
```  

## Usage

The dashboard consists of a main Python `run.py` script:

```bash
python run.py
```

Running this file with Python will launch a local Dash application in your browser.

### Folder Structure

- **`app/`**  
  Contains static content such as CSS styles, textual info, and supporting data files used in the dashboard.
  - **`assets/`**
  Text.
  - **`callbacks/`**
  Text.
  - **`components/`**
  Text.
  - **`services/`**
  Text.
  - **`app.py`**
  Text.
  - **`layout.py`**
  Text.
  
- **`data/`**  
  Contains the main dashboard logic, including data loading, indicator calculations, and plot functions.



## Features

- Interactive visualizations of lakes and catchments
- Classifcation of lake sensitivtiy and external load

## Data Sources
...
