import random
rounds = int(input("Número de rondas (impar y entre 3 y 15): "))

while rounds % 2 == 0 or rounds < 3 or rounds > 15:
    rounds = int(input("Número de rondas no válido. Debe ser impar y estar entre 3 y 15: "))

p1 = input("Jugador 1: ")
p2 = input("Jugador 2: ")

while p1.lower() == p2.lower():
    print("Los nombres no pueden ser iguales")
    p1 = input("Jugador 1: ")
    p2 = input("Jugador 2: ")

p1points = 0
p2points = 0

for i in range(rounds):
    print(f"Ronda {i+1} de {rounds}")
    r = [random.randint(1, 6) for i in range(4)]
    sum1 = r[0] + r[1]
    sum2 = r[2] + r[3]
    print(f"{p1}: {r[0]} + {r[1]} {sum1}")
    print(f"{p2}: {r[2]} + {r[3]} {sum2}")
    p1points += sum1
    p2points += sum2
