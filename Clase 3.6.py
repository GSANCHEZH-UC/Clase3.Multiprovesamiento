from multiprocessing import Process, cpu_count
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time

def analizar_categoria( df, categoria, dato ):
    by_category = df.groupby(categoria)[dato].sum().reset_index()
    by_category = by_category.sort_values(by=dato, ascending=False)
    print(f"\nAnálisis por {categoria}:")
    print(by_category)
    

def main():
  inicio = time.time()
  try:
        ventas = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales.csv", sep=",")
        print("Archivo de ventas cargado exitosamente.")
  except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

  try:
        productos = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/products.csv", sep=",")
        print("Archivo de productos cargado exitosamente.")
  except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

  try:
        clientes = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/customers.csv", sep=",")
        print("Archivo de clientes cargado exitosamente.")
  except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

  try:
        tiendas = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/stores.csv", sep=",")
        print("Archivo de tiendas cargado exitosamente.")
  except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

  try:
        fechas = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/calendar.csv", sep=",")
        print("Archivo de fechas cargado exitosamente.")
  except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

  fin = time.time()
  print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")
  input("Presiona Enter para continuar...")

  # Convertir columnas de fecha a formato datetime
  ventas['order_date'] = pd.to_datetime(ventas['order_date'])
  clientes['join_date'] = pd.to_datetime(clientes['join_date'])
  fechas['date'] = pd.to_datetime(fechas['date'])

  # Unir ventas con productos
  df_completo = pd.merge(ventas, productos, on='product_id', how='left')

  # Unir el resultado con clientes
  df_completo = pd.merge(df_completo, clientes, on='customer_id', how='left')

  # Unir el resultado con tiendas
  df_completo = pd.merge(df_completo, tiendas, on='store_id', how='left')

  # Unir el resultado con calendario por la fecha
  df_completo = pd.merge(df_completo, fechas, left_on='order_date', right_on='date', how='left')

  df_completo.info()
  input("Presiona Enter para continuar...")

  # Rellenar valores nulos en 'cocoa_percent' y 'weight_g' con la media de cada columna  
  mediacocoa_percent = df_completo['cocoa_percent'].mean()
  df_completo['cocoa_percent'] = df_completo['cocoa_percent'].fillna(mediacocoa_percent)
  
  # Rellenar valores nulos en 'weight_g' con la media de la columna
  mediaweight_g = df_completo['weight_g'].mean()
  df_completo['weight_g'] = df_completo['weight_g'].fillna(mediaweight_g)

  inicio_analisis = time.time()
  
  a = Process(target=analizar_categoria, args=(df_completo, 'category', 'revenue'))
  b = Process(target=analizar_categoria, args=(df_completo, 'gender', 'revenue'))
  c = Process(target=analizar_categoria, args=(df_completo, 'city', 'revenue'))

  a.start()
  b.start()
  c.start()
  a.join()
  b.join()
  c.join()

  
  fin_analisis = time.time()
  print(f"Tiempo de análisis: {fin_analisis - inicio_analisis:.2f} segundos")

 
if __name__ == "__main__":
  main()