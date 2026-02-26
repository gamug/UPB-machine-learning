from src import hidrogeology

import os, pickle
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def get_model_inputs(lat: float, lng: float) -> str:
    subset = pd.DataFrame({'lat': [lat], 'lng': [lng]})
    gdf = gpd.GeoDataFrame(subset, geometry=[Point(xy) for xy in zip(subset['lng'], subset['lat'])], crs="EPSG:4326")
    gdf = gdf.to_crs(hidrogeology.crs)
    gdf = gpd.sjoin(gdf, hidrogeology, how="left", predicate="within")
    return [gdf.geometry.iloc[0].x, gdf.geometry.iloc[0].y, gdf.class_hidr.iloc[0]]

def apply_model(pipeline, le, lat:float, lon: float) -> str:
    X = get_model_inputs(lat, lon)
    cats = pd.DataFrame({'class_hidr': [X[-1]]}).dropna()
    if not len(cats):
        return 'El punto seleccionado no pertenece al departamento de la Guajira'
    X = pd.DataFrame({col: [val] for col, val in zip(['X', 'Y', 'class_hidr'], X)})
    return le.inverse_transform(pipeline.predict(X))[0]