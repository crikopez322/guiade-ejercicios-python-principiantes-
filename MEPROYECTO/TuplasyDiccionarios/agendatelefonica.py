agenda = {}
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto agregado: {nombre} -> {telefono}")
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre}")
        return agenda[nombre]
    else:
        print(f"Contacto no encontrado: {nombre}")
        return None
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto eliminado: {nombre}")
    else:
        print(f"Error: {nombre} no existe en la agenda")
agregar_contacto("Juan", "123-4567")
buscar_contacto("Juan")
eliminar_contacto("Juan")