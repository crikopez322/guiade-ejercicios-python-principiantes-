lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]
it = iter(lista_principal)
es_sub = all(item in it for item in subsecuencia)
print(f"{subsecuencia} es subsecuencia de {lista_principal}: {es_sub}")