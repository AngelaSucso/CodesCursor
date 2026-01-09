# Ejercicios Simples

## Descripción General

Este repositorio contiene ejercicios prácticos independientes del curso. Cada archivo representa un ejercicio diferente que permite practicar diferentes conceptos de programación en Python.

## Archivos

### calculadora.py

Calculadora interactiva que permite realizar operaciones básicas (suma, resta, multiplicación y división) con dos números. El programa se ejecuta en un bucle continuo hasta que el usuario ingrese "salir" como operación. Incluye manejo de errores para la división por cero.

### fizzbuzz.py

Implementación del juego clásico FizzBuzz que recorre los números del 1 al 50. El programa imprime:
- "FizzBuzz" si el número es múltiplo de 3 y 5
- "Fizz" si el número es múltiplo de 3
- "Buzz" si el número es múltiplo de 5
- El número en caso contrario

### analisis.py

Script de análisis de datos que lee información desde un archivo CSV y realiza cálculos estadísticos. El programa:
- Lee datos desde el archivo `ejemplo.csv`
- Calcula estadísticas descriptivas (media, mediana y desviación estándar) para cada columna numérica
- Genera un gráfico de dispersión (scatter plot) comparando las dos columnas del archivo

**Nota:** Este script trabaja con el archivo `ejemplo.csv` que debe estar presente en el mismo directorio.

## Entorno Virtual

Se ha utilizado un entorno virtual de Python para aislar las dependencias del proyecto y evitar conflictos entre diferentes versiones de paquetes. Esto es especialmente importante para el archivo `analisis.py`, ya que requiere bibliotecas externas como `matplotlib` para la generación de gráficos y `statistics` (aunque esta última es parte de la biblioteca estándar).

El entorno virtual permite mantener las dependencias del proyecto separadas del sistema Python global, lo que facilita la gestión de versiones específicas de las bibliotecas necesarias y evita problemas de compatibilidad con otros proyectos.
