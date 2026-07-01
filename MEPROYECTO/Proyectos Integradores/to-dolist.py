tareas = []
def agregar_tarea(nombre, prioridad):
    tareas.append({"nombre": nombre, "prioridad": prioridad})
def mostrar_tareas():
    tareas_ordenadas = sorted(tareas, key=lambda x: x['prioridad'])
    for i, t in enumerate(tareas_ordenadas, 1):
        p_texto = {1: "ALTA", 2: "MEDIA", 3: "BAJA"}[t['prioridad']]
        print(f"{i}. [{p_texto}] {t['nombre']}")
agregar_tarea("Documentar", 3)
agregar_tarea("Completar proyecto", 1)
agregar_tarea("Revisar código", 2)
print("Tareas ordenadas por prioridad:")
mostrar_tareas()