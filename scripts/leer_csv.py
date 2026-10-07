# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
# TODO 3: imprime las primeras filas para revisar las columnas
# Leemos el csv con la r para que python sepa que es un directorio
import pandas as pd
datos = r"C:\Users\P05E002-Ch\Documents\programacion y estadistica\IDSD422-lab1-lectura-datos\data\ventas.csv"
df = pd.read_csv(datos)
# Imprimir el cvs 
df
# Imprimir las dimensiones
df.shape
# Imprimir los 5 primeros registros
df.head()
# Imprimir los tipos de columnas
df.columns