from collections import Counter
texto = """Python es un lenguaje de programación. 
Es muy popular en la actualidad. Python es versátil."""
texto_limpio = texto.replace('.', '').lower()
palabras = texto_limpio.split()
total_palabras = len(palabras)
frecuencia = Counter(palabras)
palabra_mas_frecuente, cuenta = frecuencia.most_common(1)[0]
longitud_promedio = sum(len(p) for p in palabras) / total_palabras
oraciones = texto.count('.')
print(f"Estadísticas del texto:")
print(f"- Palabras totales: {total_palabras}")
print(f"- Palabra más frecuente: '{palabra_mas_frecuente.capitalize()}' ({cuenta} veces)")
print(f"- Longitud promedio: {longitud_promedio:.1f} caracteres")
print(f"- Oraciones: {oraciones}")