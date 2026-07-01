texto = "programacion en python"
frecuencias = {}
for char in texto:
    if char in frecuencias:
        frecuencias[char] += 1
    else:
        frecuencias[char] = 1
print(f"Frecuencia de caracteres: {frecuencias}")