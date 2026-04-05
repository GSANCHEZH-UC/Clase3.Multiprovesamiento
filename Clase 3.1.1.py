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
    ventas1 = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales1.csv", sep=",")
    print("Archivo de ventas1 cargado exitosamente.")
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

try:
    ventas2 = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales2.csv", sep=",")
    print("Archivo de ventas2 cargado exitosamente.")
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

try:
    ventas3 = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales3.csv", sep=",")
    print("Archivo de ventas3 cargado exitosamente.")
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

try:
    ventas4 = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales4.csv", sep=",")
    print("Archivo de ventas4 cargado exitosamente.")
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

try:
    ventas5 = pd.read_csv("Chocolate Sales Dataset 2023 - 2024/sales5.csv", sep=",")
    print("Archivo de ventas5 cargado exitosamente.")
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit(1)

fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio:.2f} segundos")