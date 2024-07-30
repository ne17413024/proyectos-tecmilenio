import geopandas as gpd
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from shapely.geometry import Point

# Función para generar un número aleatorio
def numero(minimo, maximo):
    return random.randint(minimo, maximo)

# Leer el archivo de forma de los estados mexicanos
gdf = gpd.read_file("tec-proyectos/mapas/mexican-states-master/mexican-states.shp")


fig, ax = plt.subplots()

points = []

def init():
    gdf.plot(ax=ax, edgecolor='white', facecolor='black')
    return []

def update(frame):
    global points
    for point in points:
        point.remove()
    
    points = []
    # Generar nuevas coordenadas y crear los puntos
    for _ in range(50):
        print("va en: ", _)
        while True:
            #nuevos valores            85,116           15   ,33
            lon_new, lat_new = -numero(85, 116), numero(15, 33)
            point_geom = Point(lon_new, lat_new)
            if gdf.contains(point_geom).any():
                point, = ax.plot(lon_new, lat_new, 'ro', color=random.choice(["gray", "red", "green", "yellow"]), markersize=10)
                #point, = ax.plot(-93, 15, 'ro', color= "blue", markersize=15)
                points.append(point)
                break
    return points
ani = FuncAnimation(fig, update, frames=None, init_func=init, interval=500, blit=False)
plt.show()