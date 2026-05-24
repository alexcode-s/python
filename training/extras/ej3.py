import random

n_dados = int(input("Número de dados: "))
todos_iguales = False
intentos = 0
conteo = [0] * 6

opciones = [1, 2, 3, 4, 5, 6, 6, 6]

while not todos_iguales:
    dados = [random.choice(opciones) for _ in range(n_dados)]
    intentos += 1

    for d in dados:
        conteo[d - 1] += 1

    print(" – ".join(str(d) for d in dados))
    todos_iguales = len(set(dados)) == 1

total_dados = intentos * n_dados

for i in range(6):
    porcentaje = conteo[i] / total_dados * 100
    print(f"El número {i + 1} ha salido el {porcentaje:.2f} % de las veces")

print(f"He tenido que tirar los dados {intentos} veces para que salgan todos iguales")