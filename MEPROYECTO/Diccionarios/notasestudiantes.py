notas = {"Ana": 85, "Luis": 92, "Carlos": 78}
valores_notas = notas.values()
promedio = sum(valores_notas) / len(valores_notas)
estudiante_estrella = max(notas, key=notas.get)
nota_maxima = notas[estudiante_estrella]
print("Promedio de notas:", promedio)
print(f"Estudiante con mayor nota: {estudiante_estrella} ({nota_maxima})")