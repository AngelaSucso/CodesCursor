# Gestor de Tareas

Aplicación web de gestión de tareas desarrollada con Flask que permite crear, completar, editar y eliminar tareas de manera sencilla. Las tareas se almacenan de forma persistente en un archivo JSON.

## Estructura del Proyecto

```
gestor_tareas/
├── app.py                 # Aplicación principal Flask con rutas y lógica de negocio
├── templates/
│   └── index.html        # Plantilla HTML principal de la interfaz de usuario
├── static/
│   └── style.css         # Estilos CSS para la interfaz
├── tareas.json           # Archivo JSON para persistencia de datos
└── README.md             # Este archivo
```

### Descripción de Archivos y Carpetas

- **`app.py`**: Contiene la aplicación Flask principal. Define las rutas, funciones para gestionar tareas (agregar, completar, editar, eliminar) y la lógica de persistencia de datos en JSON.

- **`templates/`**: Carpeta que contiene las plantillas HTML de Jinja2.
  - **`index.html`**: Plantilla principal que renderiza la lista de tareas y los formularios para interactuar con ellas.

- **`static/`**: Carpeta para archivos estáticos (CSS, JavaScript, imágenes).
  - **`style.css`**: Hoja de estilos que proporciona el diseño visual de la aplicación con un diseño moderno y responsive.

- **`tareas.json`**: Archivo JSON que almacena las tareas de forma persistente. Contiene la lista de tareas y el ID incremental para nuevas tareas.

## Requisitos

- **Python 3.6 o superior**
- **Flask**: Framework web de Python

## Instalación y Ejecución

### Paso 1: Crear y activar entorno virtual

En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

En Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar dependencias

```bash
pip install flask
```

### Paso 3: Ejecutar la aplicación

```bash
python app.py
```

### Paso 4: Acceder a la aplicación

Abre tu navegador web y visita:
```
http://127.0.0.1:5000/
```

La aplicación estará ejecutándose en modo debug, por lo que los cambios en el código se reflejarán automáticamente al recargar la página.

## Funcionalidades

- **Agregar tareas**: Permite crear nuevas tareas ingresando texto en el formulario principal.

- **Completar tareas**: Marca las tareas como completadas, mostrándolas con texto tachado.

- **Editar tareas**: Permite modificar el texto de una tarea existente mediante un formulario inline.

- **Eliminar tareas**: Elimina tareas de la lista de manera permanente.

- **Persistencia en archivo JSON**: Todas las operaciones se guardan automáticamente en el archivo `tareas.json`, por lo que los datos persisten entre sesiones de la aplicación.

## Características Adicionales

- Interfaz de usuario moderna y responsive
- Ordenamiento automático de tareas (incompletas primero, luego completadas)
- Validación de formularios
