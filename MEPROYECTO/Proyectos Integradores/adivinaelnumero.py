import random
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False
print("¡Adivina el número entre 1 y 100!")
while not adivinado:
    intento_usuario = int(input("Introduce tu número: "))
    intentos += 1
    if intento_usuario < numero_secreto:
        print("Muy bajo")
    elif intento_usuario > numero_secreto:
        print("Muy alto")
    else:
        print(f"¡Adivinaste! El número era {numero_secreto}")
        print(f"Intentos: {intentos}")
        adivinado = True