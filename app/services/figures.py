import plotly.express as px
import pandas as pd

world_cover_legend = {
    10: "Tree Cover",
    20: "Shrubland",
    30: "Grassland",
    40: "Cropland",
    50: "Built-up",
    60: "Bare / Sparse Vegetation",
    70: "Snow and Ice",
    80: "Permanent Water Bodies",
    90: "Herbaceous Wetland",
    95: "Mangroves",
    100: "Moss and lichen",
}

hwsd_legend = {
    0: "Water bodies / non-soil",
    1: "Excessively drained",
    2: "Somewhat excessively drained",
    3: "Well drained",
    4: "Moderately well drained",
    5: "Imperfectly drained",
    6: "Poorly drained",
    7: "Very poorly drained",
}

def color_from_class(cls):
    return {
        1: '#00B0F0',
        2: '#92D050',
        3: '#FFFF00',
        4: '#FF0000',
        "Type 1": '#00B0F0',
        "Type 2": '#92D050',
        "Type 3": '#FFFF00',
        "Type 4": '#FF0000',
        0: '#d9d9d9'
    }.get(cls, '#d9d9d9')

def generate_lake_sunburst(df, classes):
    """
    Generates a sunburst plot for a single lake entity using a dataframe and classification dict.
    
    Parameters:
    - df: A pandas DataFrame (single row) or Series containing the raw attribute values.
          Column names should correspond to those in attributes_to_dataframe().
    - classes: A dictionary containing the classification results (e.g. {'Lake Type': 'Type A'}).
    """
    # 1. Handle Input: Ensure we are working with a single row of data
    if isinstance(df, pd.DataFrame):
        if len(df) > 1:
            print("Warning: DataFrame contains multiple rows. Using the first row.")
        # Squeeze the dataframe to a Series/dict-like object for easy access
        data = df.iloc[0] 
    else:
        data = df

    # 2. Define Groups
    inherent_keys = ['Water Exchange', 'Lake Depth', 'Thermal Stratification']
    nutrient_keys = [k for k in classes if k not in inherent_keys and k not in ["Lake Type", "Inherent Sensitivity", "Nutrient Supply"]]

    # 3. Map Data: Link Class Keys to DataFrame Columns
    val_map = {
        "Lake Depth":             (data.get("Lake Mean Depth (m)"), "m"),
        "Water Exchange":         (data.get("Water Exchange"), ""),
        "Thermal Stratification": (data.get("Thermal Stratification"), "%"),
        "Relief Ratio":           (data.get("Relief Ratio"), ""),
        "Population Density":     (data.get("Population Density (people/km²)"), "ppl/km²"),
        "% Depressions":          (data.get("% Depressions"), "%"),
        "Soil Drainage":          (hwsd_legend[data.get("Dominant Soil Drainage")], ""), 
        "Dominant Land Cover":    (world_cover_legend[data.get("Dominant Land Cover")], ""),
        "Catchment Runoff":       (data.get("Catchment Runoff (mm/year)"), "mm/yr"),
        "Catchment Area":         (data.get("Catchment Area (km²)"), "km²"),
        "Ohle Index":             (data.get("Ohle Index"), ""),
        "Lake Outflow":           ("Yes" if data.get("Lake Outflow") else "No" if data.get("Lake Outflow") is not None else "Unknown", ""),
    }

    # 4. Colors
    type_color = color_from_class(classes.get("Lake Type"))
    layer_colors = {
        "Inherent Sensitivity": color_from_class(classes.get("Inherent Sensitivity")),
        "Nutrient Supply": color_from_class(classes.get("Nutrient Supply"))
    }

    # 5. Build Plot Data
    names = [classes.get("Lake Type")]
    parents = [""]
    values = [1]
    colors = [type_color]
    lake_id = data.get("ID", "N/A")
    hover_text = [f"ID: {lake_id}"] 

    # Add Mid-Layers (Sensitivity / Nutrient Supply)
    for mid in ["Inherent Sensitivity", "Nutrient Supply"]:
        names.append(mid)
        parents.append(classes.get("Lake Type"))
        values.append(1)
        colors.append(layer_colors[mid])
        hover_text.append(classes.get(mid))

    # Add Outer Layers (Specific Attributes)
    for key in inherent_keys + nutrient_keys:
        if key in ["Lake Type", "Inherent Sensitivity", "Nutrient Supply"]:
            continue
        
        group = "Inherent Sensitivity" if key in inherent_keys else "Nutrient Supply"
        class_val = classes[key]
        
        names.append(key.replace(" ", "<br>")) # Line break for visual clarity
        parents.append(group)
        values.append(1)
        colors.append(color_from_class(class_val))
        
        # Generate Hover Text
        if key in val_map:
            raw_val, unit = val_map[key]
            # Handle None or NaN values gracefully
            if pd.isna(raw_val):
                val_str = "N/A"
            elif isinstance(raw_val, (int, float)):
                val_str = f"{raw_val:.2f} {unit}".strip()
            else:
                val_str = f"{raw_val} {unit}".strip()
        else:
            val_str = "N/A"

        hover_text.append(f"Class: {class_val}<br>Value: {val_str}")

    # 6. Create Plot
    plot_df = pd.DataFrame({
        "names": names,
        "parents": parents,
        "values": values,
        "color": colors,
        "hover_text": hover_text
    })

    fig = px.sunburst(plot_df, 
                      names="names", 
                      parents="parents", 
                      color="color",
                      color_discrete_map={c: c for c in set(colors)},
                      custom_data=["hover_text"]) # Pass custom data
    
    fig.update_layout(
        {'plot_bgcolor': 'rgba(0,0,0,0)', 'paper_bgcolor': "rgba(0,0,0,0)"},
        margin=dict(t=10, l=10, r=10, b=10),
        #width=300,
        #height=300,
    )
    
    fig.update_traces(
        insidetextfont=dict(size=12), 
        textfont=dict(size=16),
        marker_line_color='rgba(128,128,128,.5)',
        marker_line_width=2,
        leaf=dict(opacity=1),
        hovertemplate='<b>%{label}</b><br>%{customdata[0]}<extra></extra>'
    )
    
    return fig