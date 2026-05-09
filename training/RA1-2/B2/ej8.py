# Programa que pida un número por teclado y escriba todos sus divisores
# separados por comas (y evitando poner una coma al final).

n = int(input("Número: "))
nums = []

for i in range(1, n+1):
    if n % i == 0:
        nums.append(i)

print(f"Divisores del número {n}: ", end="")
print(*nums, sep=", ")