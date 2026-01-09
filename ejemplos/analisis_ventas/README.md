# Análisis de Ventas Mensuales

Este proyecto realiza un análisis de ventas mensuales utilizando Python, procesando datos de transacciones comerciales para calcular métricas de ventas, identificar productos destacados y generar visualizaciones.

## Archivos del Proyecto

- **`analisis.py`**: Script principal de Python que ejecuta el análisis completo. Lee los datos de ventas, calcula totales por mes, identifica productos más vendidos y genera gráficos de barras.

- **`ventas.csv`**: Archivo CSV con los datos de ventas. Contiene las columnas: `fecha`, `producto`, `cantidad` y `precio`.

- **`informe.md`**: Documento markdown con los resultados detallados del análisis, tablas resumen, interpretación de los datos y conclusiones.

- **`ventas_por_mes.png`**: Gráfico de barras generado automáticamente que muestra las ventas totales por cada mes del período analizado.

- **`top5_productos.png`**: Gráfico de barras que muestra los 5 productos con mayores ingresos.

## Requisitos

Para ejecutar este proyecto necesitas:

- **Python** 3.x
- **pandas**: Biblioteca para manipulación y análisis de datos
- **matplotlib**: Biblioteca para generación de gráficos

### Instalación de dependencias

```bash
pip install pandas matplotlib
```

## Ejecución

Para ejecutar el análisis, ejecuta el siguiente comando en la terminal desde el directorio del proyecto:

```bash
python analisis.py
```

El script:
1. Procesa el archivo `ventas.csv`
2. Calcula las ventas por mes y productos más destacados
3. Muestra los resultados en la consola
4. Genera y guarda los gráficos (`ventas_por_mes.png` y `top5_productos.png`)
5. Muestra los gráficos en ventanas separadas

## Resultados

Los resultados numéricos y las conclusiones detalladas del análisis se encuentran documentados en el archivo `informe.md`.
