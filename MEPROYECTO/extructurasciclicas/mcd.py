a, b = 48, 18
while b != 0:
    a, b = b, a % b
print(f"MCD de 48 y 18: {a}")