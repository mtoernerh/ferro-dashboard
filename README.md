# FERRO Dashboard

Dashboard for the **FERRO** project, providing an interactive overview of existing lakes and associated catchments, along with a classification of eutrophication risk based on lake sensitivity and external nutrient loading.

The dashboard is built using **Dash** and **Dash Leaflet** and is intended as an exploratory and decision-support tool for assessing eutrophication vulnerability at the lake–catchment scale.

## Requirements

A Python environment with the following packages:

- `dash`
- `dash-leaflet`
- `pandas`
- `geopandas`
- `shapely`
- `plotly`
- `pyproj`  

Clone the repository and create the environment using the provided `environment.yml` file:  
```bash
git clone <repo-url>
cd ferro-dashboard
conda env create -f environment.yml
conda activate ferro-dashboard
```  

## Usage

The dashboard is launched via the main Python script `run.py`:

```bash
python run.py
```

Running this file will start a local Dash server and open the application in your default web browser.

### Folder Structure

- **`app/`**  
  Contains the core Dash application structure and UI logic.
  - **`assets/`**  
  Static assets such as CSS stylesheets, icons, and other static resources automatically loaded by Dash.
  - **`callbacks/`**  
  Callback functions defining interactive behavior between UI components (e.g. map interaction, dropdown selections, and dynamic updates).
  - **`components/`**  
  Reusable Dash components used to build the layout (maps, plots, controls, legends, etc.).
  - **`services/`**  
  Helper functions and services for data access, preprocessing, and shared logic used across callbacks and components.
  - **`app.py`**  
  Dash application initialization, including app configuration and server setup.
  - **`layout.py`**  
  Definition of the overall dashboard layout and page structure.
  
- **`data/`**  
  Contains the local data, but also hosted on huggingface.

## Features

- Interactive visualizations of lakes and catchments
- Classifcation of lake sensitivtiy and external load

## Data Sources
...
