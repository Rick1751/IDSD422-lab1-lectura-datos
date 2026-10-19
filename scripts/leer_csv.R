# leer_csv.R — Cargar el reporte CSV del ERP (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_csv.R

# TODO 1: carga data/ventas.csv con readr::read_csv en un data.frame
datos <- readr::read_csv("data/ventas.csv", show_col_types = FALSE)

# TODO 2: imprime las dimensiones (dim) del data.frame
print(dim(datos))

# TODO 3: imprime las primeras filas (head) para revisar las columnas
print(head(datos))
