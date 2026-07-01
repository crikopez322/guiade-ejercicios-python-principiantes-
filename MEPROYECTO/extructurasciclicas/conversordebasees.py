decimal = 42
binario = ""
n = decimal
while n > 0:
    residuo = n % 2
    binario = str(residuo) + binario 
    n = n // 2 
print(f"{decimal} en binario: {binario}")