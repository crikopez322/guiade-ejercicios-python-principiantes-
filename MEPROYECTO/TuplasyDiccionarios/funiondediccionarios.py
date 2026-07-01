dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 35}
fusion = dict1.copy()
for clave, valor in dict2.items():
    if clave in fusion:
        fusion[clave] += valor
    else:
        fusion[clave] = valor
print(f"Diccionarios fusionados: {fusion}")