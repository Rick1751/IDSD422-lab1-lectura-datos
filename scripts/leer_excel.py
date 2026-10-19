# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
import pandas as pd

# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
df = pd.read_excel("data/ventas.xlsx", sheet_name="ventas", engine="openpyxl")

# TODO 3: imprime las dimensiones y las primeras filas
print("Dimensiones:", df.shape)
print(df.head())
