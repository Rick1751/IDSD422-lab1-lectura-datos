# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
import json

import pandas as pd

# TODO 2: carga data/ventas.json con json.load
with open("data/ventas.json", encoding="utf-8") as archivo:
    registros = json.load(archivo)

# TODO 3: convierte la lista de diccionarios en un DataFrame
#         (recuerda del cap. 2: el JSON no llega como tabla directa)
df = pd.json_normalize(registros)

# TODO 4: imprime las dimensiones y las primeras filas
print("Dimensiones:", df.shape)
print(df.head())
