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
    ('clientes', os.path.join(base_path, 'customers.csv')),
    ('productos', os.path.join(base_path, 'products.csv')),
    ('tiendas', os.path.join(base_path, 'stores.csv')),
    ('calendario', os.path.join(base_path, 'calendar.csv'))
]

inicio = time.time()

# Uso de ThreadPoolExecutor para hacer varios proceso de carga a la vez

with ThreadPoolExecutor(max_workers=5) as executor: # max_workers define el número de procesos en paralelo
    # executor.map lanza todos los proceso con la llamada a cargar_archivo 
    # cada proceso toma una de las tuplas de archivos_a_cargar
    # en  lista_resultados queda la lista de los DataSets devueltos por la función cargar_archivo
    lista_resultados = list(executor.map(cargar_archivo, archivos_a_cargar)) 


fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio:.5f} segundos")
input("Presiona Enter para continuar...")

ventas_df = dict(lista_resultados)['ventas']
clientes_df = dict(lista_resultados)['clientes']
productos_df = dict(lista_resultados)['productos']
tiendas_df = dict(lista_resultados)['tiendas']
calendario_df = dict(lista_resultados)['calendario']

print("DataFrames cargados:")
print(f"Ventas: {ventas_df.shape[0]} filas, {ventas_df.shape[1]} columnas")
print(f"Clientes: {clientes_df.shape[0]} filas, {clientes_df.shape[1]} columnas")
print(f"Productos: {productos_df.shape[0]} filas, {productos_df.shape[1]} columnas")
print(f"Tiendas: {tiendas_df.shape[0]} filas, {tiendas_df.shape[1]} columnas")
print(f"Calendario: {calendario_df.shape[0]} filas, {calendario_df.shape[1]} columnas")

