# leer_json.R — Cargar el reporte JSON de la API (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_json.R

# TODO 1: carga data/ventas.json con jsonlite::fromJSON
datos <- jsonlite::fromJSON("data/ventas.json")

# TODO 2: convierte el resultado en data.frame si hace falta
datos <- as.data.frame(datos)

# TODO 3: imprime las dimensiones (dim) y las primeras filas (head)
print(dim(datos))
print(head(datos))
