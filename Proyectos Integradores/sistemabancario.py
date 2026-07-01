banco = {}
def crear_cuenta(numero, titular, saldo_inicial, tipo):
    banco[numero] = {"titular": titular, "saldo": saldo_inicial, "tipo": tipo, "historial": []}
def depositar(numero, cantidad):
    banco[numero]["saldo"] += cantidad
    banco[numero]["historial"].append(("Depósito", cantidad))
def retirar(numero, cantidad):
    if banco[numero]["saldo"] >= cantidad:
        banco[numero]["saldo"] -= cantidad
        banco[numero]["historial"].append(("Retiro", -cantidad))
    else:
        print("Fondos insuficientes")
crear_cuenta(1001, "Juan Pérez", 1500, "Ahorros")
depositar(1001, 500)
retirar(1001, 200)
cuenta = banco[1001]
print(f"Cuenta #1001: {cuenta['titular']}")
print(f"Saldo: ${cuenta['saldo']}")