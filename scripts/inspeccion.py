# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
import pandas as pd

df = pd.read_csv("data/ventas.csv")

# TODO 2: imprime los tipos (dtypes) de cada columna
print("Tipos de datos:")
print(df.dtypes)

# TODO 3: crea la columna derivada "ticket" = ventas / clientes
df["ticket"] = df["ventas"] / df["clientes"]

# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
venta_promedio = df["ventas"].mean()
ticket_promedio = df["ventas"].sum() / df["clientes"].sum()
sucursal_mayor = df.loc[df["ventas"].idxmax(), "sucursal"]
sucursal_menor = df.loc[df["ventas"].idxmin(), "sucursal"]
ventas_por_region = df.groupby("region")["ventas"].sum()
region_mayor = ventas_por_region.idxmax()

print("Venta promedio por sucursal:", venta_promedio)
print("Ticket promedio:", ticket_promedio)
print("Sucursal con mayor venta:", sucursal_mayor)
print("Sucursal con menor venta:", sucursal_menor)
print("Región con mayor venta total:", region_mayor)
print("Ventas totales por región:")
print(ventas_por_region)
