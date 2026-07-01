lado1 = int(input("ingresa el primer lado: "))
lado2 = int(input("ingresa el segundo lado: "))
lado3 = int(input("ingresa el tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("¡sí forman un triángulo!")
else:
    print("no pueden formar un triángulo.")