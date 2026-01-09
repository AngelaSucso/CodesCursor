from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

# Lista global de tareas y variable de id incremental
tareas = []
proximo_id = 1

# Archivo JSON para persistencia
ARCHIVO_TAREAS = 'tareas.json'

def cargar_datos():
    """Carga las tareas y el próximo ID desde el archivo JSON"""
    global tareas, proximo_id
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                tareas = datos.get('tareas', [])
                proximo_id = datos.get('proximo_id', 1)
        except (json.JSONDecodeError, IOError):
            # Si hay error leyendo el archivo, empezar con valores por defecto
            tareas = []
            proximo_id = 1

def guardar_datos():
    """Guarda las tareas y el próximo ID en el archivo JSON"""
    datos = {
        'tareas': tareas,
        'proximo_id': proximo_id
    }
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

# Cargar datos al inicio de la aplicación
cargar_datos()
    
# Esta función agrega una nueva tarea a la lista de tareas, le asigna un id único incremental y la marca como incompleta por defecto. 
# Luego actualiza el archivo de persistencia y devuelve la tarea creada.
def agregar_tarea(texto):
    global tareas, proximo_id
    tarea = {'id': proximo_id, 'texto': texto, 'completada': False}
    tareas.append(tarea)
    proximo_id += 1
    guardar_datos()
    return tarea
    
# Esta función busca una tarea por su id, la marca como completada, guarda los datos y devuelve la tarea modificada. 
# Si no la encuentra, devuelve None.
def completar_tarea(id):
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            guardar_datos()
            return tarea
    return None

# Esta función elimina una tarea de la lista dado su id, actualiza el archivo de persistencia y devuelve True si la tarea fue eliminada.
def eliminar_tarea(id):
    global tareas
    for i, tarea in enumerate(tareas):
        if tarea['id'] == id:
            tareas.pop(i)
            guardar_datos()
            return True
    return False

# Esta función edita el texto de una tarea existente dado su id.
# Busca la tarea en la lista, actualiza su texto, guarda los cambios y devuelve la tarea modificada.
# Si no encuentra la tarea, retorna None.
def editar_tarea(id, nuevo_texto):
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['texto'] = nuevo_texto
            guardar_datos()
            return tarea
    return None

# Esta ruta maneja la página principal '/', ordena las tareas para mostrar primero las incompletas y luego las completadas, y las pasa a la plantilla index.html para renderizarlas.
@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['completada'])
    return render_template('index.html', tareas=tareas_ordenadas)

# Esta ruta recibe una nueva tarea desde el formulario, la agrega a la lista y redirige a la página principal.
@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

# Esta ruta recibe una solicitud POST para marcar como completada una tarea específica según su id.
# Llama a la función completar_tarea(id) y luego redirige al usuario a la página principal.
@app.route('/completar/<int:id>', methods=['POST'])
def completar(id):
    completar_tarea(id)
    return redirect('/')

# Esta ruta elimina una tarea específica identificada por su id mediante una solicitud POST y redirige al usuario a la página principal.
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    eliminar_tarea(id)
    return redirect('/')

# Esta ruta recibe una solicitud POST para editar el texto de una tarea específica según su id.
# Si el nuevo texto está presente, llama a la función editar_tarea(id, nuevo_texto) y redirige a la página principal.
@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nuevo_texto = request.form.get('texto_editado')
    if nuevo_texto:
        editar_tarea(id, nuevo_texto)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
