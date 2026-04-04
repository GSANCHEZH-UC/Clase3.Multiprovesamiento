import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import time

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