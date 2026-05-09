# Programa que pida un número por teclado y muestre sus divisores.

n = int(input("Número: "))
print(f"Divisores de {n}: ")

for i in range(n, 0, -1):
    if n % i == 0:
        print(i)