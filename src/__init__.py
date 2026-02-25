import os
import geopandas as gpd

hidrogeology = gpd.read_file(os.path.join('files', 'data', 'Mapa_hidrogeologico_polygon.zip'))
hidrogeology = hidrogeology[['class_hidr', 'geometry']]