# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
datos <- readr::read_csv("data/ventas.csv", show_col_types = FALSE)

# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
str(datos)
cat("region es character:", is.character(datos$region), "\n")

# TODO 3: crea la columna derivada "ticket" = ventas / clientes
datos$ticket <- datos$ventas / datos$clientes

# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
venta_promedio <- mean(datos$ventas)
ticket_promedio <- sum(datos$ventas) / sum(datos$clientes)
ventas_por_region <- aggregate(ventas ~ region, data = datos, FUN = sum)
sucursal_mayor <- datos$sucursal[which.max(datos$ventas)]
sucursal_menor <- datos$sucursal[which.min(datos$ventas)]
region_mayor <- ventas_por_region$region[which.max(ventas_por_region$ventas)]

cat("Venta promedio por sucursal:", venta_promedio, "\n")
cat("Ticket promedio:", ticket_promedio, "\n")
cat("Sucursal con mayor venta:", sucursal_mayor, "\n")
cat("Sucursal con menor venta:", sucursal_menor, "\n")
cat("Región con mayor venta total:", region_mayor, "\n")
print(ventas_por_region)
