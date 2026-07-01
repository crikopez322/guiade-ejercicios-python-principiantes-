def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
inicio, fin = 10, 50
primos = [n for n in range(inicio, fin + 1) if es_primo(n)]
print(f"Números primos entre {inicio} y {fin}: {primos}")