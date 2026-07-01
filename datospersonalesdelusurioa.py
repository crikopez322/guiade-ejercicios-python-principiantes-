from datetime import datetime
print("--- Iniciando sistema de registro ---")
anio_actual = datetime.now().year
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
mail = input("Ingrese su correo: ")
sexo = input("Ingrese su sexo: ")
phone = input("Ingrese su numero de telefono: ")
while True:
    try:
        birth_year = int(input("\nIngrese su año de nacimiento (ej. 2000): "))
        age = int(input("Ingrese su edad actual: "))
        edad_calculada = anio_actual - birth_year
        if age == edad_calculada or age == edad_calculada - 1:
            print("¡Verificación exitosa!")
            break 
        else:
            print(f"ERROR: Los datos no coinciden. Según el año {birth_year}, usted debería tener {edad_calculada} años, no {age}.")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")
print("\n--- Resumen de Datos ---")
print(f"Nombre: {name} {lastname}")
print(f"Correo: {mail}")
print(f"Año: {birth_year}, Edad: {age}") 