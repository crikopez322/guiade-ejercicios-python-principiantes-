anidada = [[1, 2], [3, 4, 5], [6]]
lista_aplanada = [elemento for sublista in anidada for elemento in sublista]
print(f"Lista aplanada: {lista_aplanada}")