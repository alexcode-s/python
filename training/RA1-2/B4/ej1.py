# Programa que pida un número por teclado y calcule su factorial.

n = int(input("Número: "))
f = []
total = 1

for i in range(n, 0, -1):
    f.append(str(i))
    total *= i

print(f"{n}! = {"*".join(f)} = {total}")