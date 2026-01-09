# Editor de Notas - Ejercicio de Tkinter

## Descripción

Este ejercicio forma parte del curso "Cursor con Python: desarrollo inteligente con IA" y consiste en una aplicación de escritorio desarrollada en Python utilizando la librería Tkinter. La aplicación implementa un editor de notas básico que permite crear, editar y gestionar archivos de texto mediante una interfaz gráfica de usuario (GUI).

## Requisitos

- **Python 3.x**: La aplicación requiere Python 3 o superior.
- **Tkinter**: Esta librería viene incluida de forma predeterminada con la instalación estándar de Python, por lo que no requiere instalación adicional.

## Ejecución

Para ejecutar la aplicación, abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:

```bash
python notas.py
```

En sistemas Linux o macOS, también puedes utilizar:

```bash
python3 notas.py
```

La aplicación se abrirá en una ventana de 600x400 píxeles con el título "Editor de Notas".

## Funcionalidades Principales

### Área de Texto

La aplicación cuenta con un área de texto multilínea donde el usuario puede escribir y editar contenido de forma libre.

### Menú Archivo

- **Abrir**: Permite seleccionar un archivo de texto existente para cargar su contenido en el editor. Soporta archivos `.txt` y otros formatos.
- **Guardar**: Permite guardar el contenido actual del editor en un archivo. Si el archivo no existe, se crea uno nuevo.
- **Salir**: Cierra la aplicación.

### Menú Editar

- **Cortar** (Ctrl+X): Elimina el texto seleccionado y lo copia al portapapeles.
- **Copiar** (Ctrl+C): Copia el texto seleccionado al portapapeles sin eliminarlo.
- **Pegar** (Ctrl+V): Inserta el contenido del portapapeles en la posición del cursor.

Todas las operaciones de edición pueden realizarse tanto desde el menú como mediante los atajos de teclado estándar.

## Programación Dirigida por Eventos

Esta aplicación utiliza el paradigma de programación dirigida por eventos, característico de las interfaces gráficas. En este modelo, el programa permanece en un bucle de espera (event loop) y responde a las acciones del usuario, como clics de mouse, pulsaciones de teclado o selección de elementos del menú. Cada interacción genera un evento que es capturado por el sistema y ejecuta la función o método correspondiente (callback). Tkinter gestiona internamente este ciclo de eventos mediante el método `mainloop()`, permitiendo que la aplicación permanezca activa y receptiva a las interacciones del usuario.
