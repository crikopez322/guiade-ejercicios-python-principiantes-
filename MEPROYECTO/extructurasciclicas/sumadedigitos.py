numero = 1234
suma = 0
n_temporal = numero
while n_temporal > 0:
    digito = n_temporal % 10
    suma += digito
    n_temporal = n_temporal // 10
print(f"Suma de dígitos de {numero}: {suma}")