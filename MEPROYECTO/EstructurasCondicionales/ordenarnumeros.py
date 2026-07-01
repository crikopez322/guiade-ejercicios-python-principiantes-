a, b, c = 15, 8, 22
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(f"Números ordenados: {a}, {b}, {c}")