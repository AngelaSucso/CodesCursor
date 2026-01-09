import csv
import statistics
import matplotlib.pyplot as plt

def calcular_estadisticas(datos):
    # Transponer filas a columnas
    columnas = list(zip(*datos))
    for i, columna in enumerate(columnas):
        try:
            numeros = [float(x) for x in columna]
            media = statistics.mean(numeros)
            mediana = statistics.median(numeros)
            desv_std = statistics.stdev(numeros) if len(numeros) > 1 else 0
            print(f"Columna {i+1}: media={media}, mediana={mediana}, desviación estándar={desv_std}")
        except ValueError:
            print(f"Columna {i+1}: no numérica")

datos = []
with open('ejemplo.csv', newline='', encoding='utf-8') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        print(fila)
        datos.append(fila)

if datos:
    calcular_estadisticas(datos)
    try:
        # Convierte col1 y col2 en flotantes para el scatter plot
        col1 = [float(fila[0]) for fila in datos]
        col2 = [float(fila[1]) for fila in datos]
        plt.scatter(col1, col2)
        plt.xlabel('Columna 1')
        plt.ylabel('Columna 2')
        plt.title('Scatter plot de Col1 vs Col2')
        plt.show()
    except (ValueError, IndexError):
        print("No se pudo graficar")
