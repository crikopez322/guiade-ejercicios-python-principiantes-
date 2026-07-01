mensaje = "Hola Mundo"
desplazamiento = 3
def cifrado_cesar(texto, desp):
    resultado = ""
    for char in texto:
        if char.isalpha():
            inicio = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - inicio + desp) % 26 + inicio)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado
cifrado = cifrado_cesar(mensaje, desplazamiento)
descifrado = cifrado_cesar(cifrado, -desplazamiento)
print(f"Mensaje cifrado: {cifrado}")
print(f"Mensaje descifrado: {descifrado}")