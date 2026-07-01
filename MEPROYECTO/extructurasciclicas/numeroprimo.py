import math
numero = 17
if numero <= 1:
    es_primo = False
else:
    es_primo = True
    limite = int(math.sqrt(numero))
    for i in range(2, limite + 1):
        if numero % i == 0:
            es_primo = False
            break 
if es_primo:
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")