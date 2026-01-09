# Organizador de Archivos

## Descripción

El script `organizar.py` es una herramienta de línea de comandos diseñada para organizar automáticamente archivos en carpetas según su tipo. El programa examina todos los archivos presentes en una carpeta objetivo y los mueve a subcarpetas predefinidas basándose en su extensión, facilitando así la organización y localización de los archivos.

## Requisitos

- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS

El script utiliza únicamente módulos estándar de Python (`sys`, `argparse`, `pathlib`), por lo que no requiere la instalación de dependencias adicionales.

## Instrucciones de Ejecución

### Ejecución desde la Terminal

El script se ejecuta desde la terminal utilizando el intérprete de Python. Asegúrese de estar en el directorio que contiene el archivo `organizar.py` o proporcione la ruta completa al script.

#### Sintaxis básica:

```bash
python organizar.py [opciones]
```

### Ejemplos de Uso

#### 1. Ejecución por defecto

Al ejecutar el script sin parámetros adicionales, se organizarán los archivos contenidos en la carpeta `Downloads` ubicada en el mismo directorio que el script:

```bash
python organizar.py
```

#### 2. Especificar una carpeta objetivo

Mediante el parámetro `-d` o `--directorio`, es posible indicar una ruta diferente a la carpeta que se desea organizar:

```bash
python organizar.py -d "C:\Users\Usuario\Escritorio"
```

O utilizando la forma completa del parámetro:

```bash
python organizar.py --directorio "C:\Users\Usuario\Documentos"
```

En sistemas Linux o macOS:

```bash
python organizar.py -d /home/usuario/Descargas
```

## Estructura de Organización

El script organiza los archivos en las siguientes carpetas según su extensión:

- **Imagenes**: `.png`, `.jpg`, `.jpeg`, `.gif`
- **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Videos**: `.mp4`, `.avi`, `.mkv`
- **Musica**: `.mp3`, `.wav`
- **Otros**: Cualquier archivo cuya extensión no coincida con las categorías anteriores

Las carpetas se crean automáticamente dentro del directorio objetivo si no existen previamente.

## Comportamiento con Archivos Duplicados

Si durante el proceso de organización se intenta mover un archivo a una carpeta donde ya existe otro archivo con el mismo nombre, el comportamiento depende del sistema operativo. En la mayoría de los casos, esto resultará en un error que interrumpirá la ejecución del script. Se recomienda revisar manualmente los archivos antes de ejecutar el script si se sospecha la presencia de archivos duplicados, o renombrar los archivos conflictivos previamente.

## Notas Adicionales

- El script solo procesa archivos, no subdirectorios. Las carpetas existentes en el directorio objetivo no se modifican.
- La organización se realiza de forma permanente: los archivos son movidos (no copiados) a sus respectivas carpetas.
- Se muestra un mensaje en la terminal por cada archivo movido, indicando el nombre del archivo y la carpeta destino.
