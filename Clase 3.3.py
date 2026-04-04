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
resultados = {}
with ThreadPoolExecutor(max_workers=5) as executor: # max_workers define el número de procesos en paralelo
    # executor.map lanza todos los proceso con la llamada a cargar_archivo 
    # cada proceso toma una de las tuplas de archivos_a_cargar
    # en  lista_resultados queda la lista de los DataSets devueltos por la función cargar_archivo
    lista_resultados = list(executor.map(cargar_archivo, archivos_a_cargar)) 


fin = time.time()
print(f"Tiempo de carga: {fin - inicio:.5f} segundos")
input("Presiona Enter para continuar...")

# Convertir la lista de resultados en DataFrames para fácil acceso
ventas_df = dict(lista_resultados)['ventas']
clientes_df = dict(lista_resultados)['clientes']
productos_df = dict(lista_resultados)['productos']
tiendas_df = dict(lista_resultados)['tiendas']
calendario_df = dict(lista_resultados)['calendario']

# Convertir columnas de fecha a formato datetime
ventas_df['order_date'] = pd.to_datetime(ventas_df['order_date'])
clientes_df['join_date'] = pd.to_datetime(clientes_df['join_date'])
calendario_df['date'] = pd.to_datetime(calendario_df['date'])

# Unir ventas con productos
df_completo = pd.merge(ventas_df, productos_df, on='product_id', how='left')

# Unir el resultado con clientes
df_completo = pd.merge(df_completo, clientes_df, on='customer_id', how='left')

# Unir el resultado con tiendas
df_completo = pd.merge(df_completo, tiendas_df, on='store_id', how='left')

# Unir el resultado con calendario por la fecha
df_completo = pd.merge(df_completo, calendario_df, left_on='order_date', right_on='date', how='left')

df_completo.info()
input("Presiona Enter para continuar...")

# Rellenar valores nulos en 'cocoa_percent' y 'weight_g' con la media de cada columna
mediacocoa_percent = df_completo['cocoa_percent'].mean()
print(f"La media de la columna 'cocoa_percent' es: {mediacocoa_percent}")
df_completo['cocoa_percent'] = df_completo['cocoa_percent'].fillna(mediacocoa_percent)
print(f"Valores nulos en 'cocoa_percent' después de rellenar con la moda: {df_completo['cocoa_percent'].isnull().sum()}")
input("Presiona Enter para continuar...")

# Rellenar valores nulos en 'weight_g' con la media de la columna
mediaweight_g = df_completo['weight_g'].mean()
print(f"La media de la columna 'weight_g' es: {mediaweight_g}")
df_completo['weight_g'] = df_completo['weight_g'].fillna(mediaweight_g)
print(f"Valores nulos en 'weight_g' después de rellenar con la moda: {df_completo['weight_g'].isnull().sum()}")
input("Presiona Enter para continuar...")

# Generar histogramas para las columnas discount, revenue y profit usando Seaborn
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Histograma para discount
sns.histplot(df_completo['discount'], ax=axes[0], kde=True)
axes[0].set_title('Histograma de Discount')
axes[0].set_xlabel('Discount')
axes[0].set_ylabel('Frecuencia')

# Histograma para revenue
sns.histplot(df_completo['revenue'], ax=axes[1], kde=True)
axes[1].set_title('Histograma de Revenue')
axes[1].set_xlabel('Revenue')
axes[1].set_ylabel('Frecuencia')

# Histograma para profit
sns.histplot(df_completo['profit'], ax=axes[2], kde=True)
axes[2].set_title('Histograma de Profit')
axes[2].set_xlabel('Profit')
axes[2].set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()
