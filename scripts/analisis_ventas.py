# ==============================================================
# REVISIÓN QA — P3 (Rol: Lucas Timotio)
# Verificaciones realizadas:
# - Rutas relativas correctas (reproducible en Colab)
# - Sin datos sensibles ni tokens en el código
# - Comentarios técnicos presentes en cada sección
# - Gráficos guardados correctamente en /resultados
# ==============================================================

# analisis_ventas.py
# Autor: P2 - Desarrollador Técnico (Rol: Ricardo Ricardo)
# Proyecto: Análisis de Ventas — Célula Ágil UTN TUP
# Issue Jira: EDDA-5

import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================================================
# CARGA DE DATOS
# Usamos ruta relativa para garantizar reproducibilidad
# en cualquier entorno (Colab, local, etc.)
# ==============================================================
df = pd.read_csv("../datos/dataset.csv")

# Convertimos la columna de fecha a tipo datetime
# para poder agrupar por mes correctamente
df["sales_date"] = pd.to_datetime(df["sales_date"])

# ==============================================================
# INDICADORES BÁSICOS
# Calculamos métricas globales del período analizado
# ==============================================================
ventas_totales = df["sales_amount"].sum()
producto_mas_vendido = df.groupby("product")["quantity"].sum().idxmax()
ventas_por_mes = df.groupby(df["sales_date"].dt.to_period("M"))["sales_amount"].sum()

print("=" * 40)
print("RESUMEN DE VENTAS")
print("=" * 40)
print(f"Ventas totales del período: ${ventas_totales:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido}")
print("\nVentas por mes:")
print(ventas_por_mes.to_string())

# ==============================================================
# GRÁFICO DE EVOLUCIÓN MENSUAL
# Visualizamos la tendencia de ventas a lo largo del tiempo
# para identificar estacionalidad o crecimiento
# ==============================================================
fig, ax = plt.subplots(figsize=(10, 5))

ventas_por_mes.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")

ax.set_title("Evolución Mensual de Ventas", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes", fontsize=11)
ax.set_ylabel("Monto Total ($)", fontsize=11)
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()

# Guardamos el gráfico en /resultados con ruta relativa
os.makedirs("../resultados", exist_ok=True)
plt.savefig("../resultados/grafico_ventas_mensuales.png", dpi=150)
print("\nGráfico guardado en /resultados/grafico_ventas_mensuales.png")

# ==============================================================
# GRÁFICO DE VENTAS POR PRODUCTO
# Comparamos el rendimiento de cada producto
# ==============================================================
fig2, ax2 = plt.subplots(figsize=(8, 5))

df.groupby("product")["sales_amount"].sum().sort_values().plot(
    kind="barh", ax=ax2, color="darkorange", edgecolor="white"
)

ax2.set_title("Ventas Totales por Producto", fontsize=14, fontweight="bold")
ax2.set_xlabel("Monto Total ($)", fontsize=11)
plt.tight_layout()

plt.savefig("../resultados/grafico_ventas_por_producto.png", dpi=150)
print("Gráfico guardado en /resultados/grafico_ventas_por_producto.png")
