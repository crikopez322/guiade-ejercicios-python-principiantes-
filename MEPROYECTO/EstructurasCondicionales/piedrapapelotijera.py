jugador1 = "piedra"
jugador2 = "tijeras"
opciones = ["piedra", "papel", "tijeras"]
if jugador1 not in opciones or jugador2 not in opciones:
    print("Entrada inválida. Por favor usa: piedra, papel o tijeras.")
else:
    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijeras" and jugador2 == "papel"):
        print(f"Jugador 1 gana: {jugador1} vence a {jugador2}")
    else:
        print(f"Jugador 2 gana: {jugador2} vence a {jugador1}")