import random

n_dados = int(input("Número de dados: "))
todos_iguales = False
intentos = 0

while not todos_iguales:
    dados = [random.randint(1, 6) for _ in range(n_dados)]
    intentos += 1
    print(" – ".join(str(d) for d in dados))
    todos_iguales = len(set(dados)) == 1

print(f"He tenido que lanzar los dados {intentos} veces para que todos sean iguales")