calificacion = int(input("ingrese su calificacion: "))

if calificacion >= 90:
    print("A - Aprobado")
elif calificacion >= 80:
    print("B - Aprobado")
elif calificacion >= 70:
    print("C - Aprobado")
elif calificacion >= 60:
    print("D - Aprobado")
else:
    print("F - Reprobado")