import folium
import time
import random
from shapely.geometry import Point
import geopandas as gpd

# Cargar el archivo de forma de los estados mexicanos
gdf = gpd.read_file("tec-proyectos/mapas/mexican-states-master/mexican-states.shp")
m = folium.Map(location=(23.634501, -102.552784), zoom_start=5)

def numero(minimo, maximo):
    return random.uniform(minimo, maximo)

def punto_dentro(punto):
    return gdf.contains(punto).any()

def generar_puntos(cantidad):
    puntos = []
    while len(puntos) < cantidad:
        lat = numero(15, 33)
        lon = -numero(85, 116)
        punto = Point(lon, lat)
        if punto_dentro(punto):
            puntos.append((lat, lon))
    return puntos

while True:
    puntos = generar_puntos(50)
    for lat, lon in puntos:
        folium.Marker(
            location=[lat, lon],
            #popup="Punto de interés",
            #icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    
    # Guardar el mapa
    m.save("tec-proyectos/mapas/index.html")
    
    # Esperar 2 segundos
    time.sleep(1)
    
    # Limpiar los puntos del mapa
    m = folium.Map(location=(23.634501, -102.552784), zoom_start=5)