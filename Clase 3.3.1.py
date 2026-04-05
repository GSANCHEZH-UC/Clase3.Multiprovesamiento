import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor

# Función a ajecutar en procesos paralelos
def cargar_archivo(info):
    nombre, ruta = info
    try:
        if os.path.exists(ruta):
            df = pd.read_csv(ruta, sep=",") # en df queda el DataSer leído del archivo "nombre"
            print(f"Cargado correctamente: {nombre}")
            return nombre, df
        else:
            print(f"Archivo no encontrado: {ruta}")
            return nombre, None
    except Exception as e:
        print(f"Error al cargar {nombre}: {e}")
        return nombre, None

# Definir ruta de acceso a los archicos de datos
base_path = 'Chocolate Sales Dataset 2023 - 2024/'

# Lista de archivos a cargar
archivos_a_cargar = [
    ('ventas', os.path.join(base_path, 'sales.csv')),
    ('ventas1', os.path.join(base_path, 'sales1.csv')),
    ('ventas2', os.path.join(base_path, 'sales2.csv')),
    ('ventas3', os.path.join(base_path, 'sales3.csv')),
    ('ventas4', os.path.join(base_path, 'sales4.csv')),
    ('ventas5', os.path.join(base_path, 'sales5.csv'))
]

inicio = time.time()

# Uso de ThreadPoolExecutor para hacer varios proceso de carga a la vez
resultados = {}
with ThreadPoolExecutor(max_workers=5) as executor: # max_workers define el número de procesos en paralelo
    # executor.map lanza todos los proceso con la llamada a cargar_archivo 
    # cada proceso toma una de las tuplas de archivos_a_cargar
    # en  lista_resultados queda la lista de los DataSets devueltos por la función cargar_archivo
    lista_resultados = list(executor.map(cargar_archivo, archivos_a_cargar)) 


fin = time.time()
print(f"Tiempo de carga: {fin - inicio:.5f} segundos")
input("Presiona Enter para continuar...")