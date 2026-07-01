registro = {
    "Ana": {"Matemáticas": [90, 85], "Historia": [88, 92]},
    "Luis": {"Matemáticas": [80, 75], "Historia": [95, 98]}
}
calificaciones_ana = []
for materias in registro["Ana"].values():
    calificaciones_ana.extend(materias)
promedio_ana = sum(calificaciones_ana) / len(calificaciones_ana)
calificaciones_mates = []
for estudiante in registro.values():
    if "Matemáticas" in estudiante:
        calificaciones_mates.extend(estudiante["Matemáticas"])
promedio_mates = sum(calificaciones_mates) / len(calificaciones_mates)
print(f"Promedio Ana: {promedio_ana}")
print(f"Promedio Matemáticas: {promedio_mates}")