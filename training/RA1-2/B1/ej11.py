import random
# Modificar el programa anterior para que tu programa tire dos dados de forma continuada hasta que el número que
# salga en ambos sea el mismo. En ese momento debería de parar la ejecución e informarnos de cuantas tiradas ha
# tenido que hacer para llegar a ese resultado

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
attempts = 1

while n1 != n2:
    print(f"{n1} : {n2}")
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    attempts += 1

print(f"{n1} : {n2}")
print(f"Número de intentos: {attempts}")
