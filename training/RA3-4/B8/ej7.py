# Programa que, dado un número introducido por teclado, averigüe si es un número Amstrong o Narcisista.

n = input("Número: ")
sums = [int(n[i]) ** len(n) for i in range(len(n))]
result = sum(sums)

print(f"El número {n} es narcisista" if result == int(n) else f"El número {n} no es narcisista")

