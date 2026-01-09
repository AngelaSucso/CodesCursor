import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo de ventas, convierte columnas a tipos numéricos y extrae el mes de la fecha
df = pd.read_csv('ventas.csv', parse_dates=['fecha'])
df['cantidad'] = pd.to_numeric(df['cantidad'], downcast='integer')
df['precio'] = pd.to_numeric(df['precio'], downcast='float')
df['mes'] = df['fecha'].dt.to_period('M')
#df.dtypes


# Calcula el total de ventas por mes sumando la multiplicación de cantidad por precio,
# luego imprime el resultado en formato de tabla.
ventas_por_mes = (
    df.assign(venta=df['cantidad'] * df['precio'])
      .groupby('mes')['venta']
      .sum()
      .sort_index()
)
#print(ventas_por_mes)
print("Ventas por mes:")
print(ventas_por_mes.to_frame())


# Este fragmento calcula el total de unidades vendidas y los ingresos por cada producto,
# identifica cuál fue el producto más vendido en unidades y cuál generó más ingresos,
# e imprime esta información.
df['ingreso'] = df['cantidad'] * df['precio']
ventas_prod = df.groupby('producto').agg({
    'cantidad': 'sum',
    'ingreso': 'sum'
})
mas_vendido = ventas_prod['cantidad'].idxmax()
mayor_ingreso = ventas_prod['ingreso'].idxmax()
print(f"\nProducto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")
print(f"Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")


# Este fragmento genera y guarda un gráfico de barras de las ventas totales por mes.
ventas_por_mes.index = ventas_por_mes.index.astype(str)
plt.figure(figsize=(6,4))
ventas_por_mes.plot(kind='bar')
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas (€)")
plt.tight_layout()
plt.savefig("ventas_por_mes.png")
plt.show()


# Este fragmento genera y guarda un gráfico de barras con los 5 productos con mayores ingresos.
top5 = ventas_prod.nlargest(5, 'ingreso')
plt.figure(figsize=(6,4))
plt.bar(top5.index, top5['ingreso'])
plt.title("Top 5 Productos por Ingresos")
plt.ylabel("Ingresos (€)")
plt.xlabel("Producto")
plt.tight_layout()
plt.savefig("top5_productos.png")
plt.show()