texto = "Anita lava la tina"
texto_limpio = texto.replace(" ", "").lower()
es_palindromo = True
longitud = len(texto_limpio)
for i in range(longitud // 2):
    if texto_limpio[i] != texto_limpio[longitud - 1 - i]:
        es_palindromo = False
        break
if es_palindromo:
    print(f"'{texto}' es un palíndromo")
else:
    print(f"'{texto}' no es un palíndromo")