# Programa que pida elegir entre cuatro destinos turísticos (Francia, Italia, Chile o Japón) y dependiendo de
# la elección diga cuál es la capital del destino (París, Roma, Santiago de Chile o Tokio)

dest = input("Destino: ")
cap = {"Francia": "París", "Italia": "Roma", "Chile": "Santiago De Chile", "Japón": "Tokio"}

print(f"Capital: {cap.get(dest)}")