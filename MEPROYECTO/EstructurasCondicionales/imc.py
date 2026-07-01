peso = 70 
altura = 1.75 
imc = peso / (altura ** 2)
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso Normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print(f"IMC: {imc:.2f} - Clasificación: {clasificacion}")