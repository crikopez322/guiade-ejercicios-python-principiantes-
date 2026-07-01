texto = "hola Mundo Python"
texto_minusculas = texto.lower()
contador_vocales = 0
vocales = "aeiou"
for letra in texto_minusculas:
    if letra in vocales:
        contador_vocales = contador_vocales + 1
print("el número de vocales es:", contador_vocales)