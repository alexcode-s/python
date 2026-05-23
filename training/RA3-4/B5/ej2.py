import math
# Programa que permita calcular todos los divisores comunes a dos números

def divisors(n):
    d = set()
    for i in range(1, n + 1):
        if n % i == 0:
            d.add(i)
    return d

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

dN1 = divisors(n1)
dN2 = divisors(n2)

print(dN1, dN2)
common = dN1 & dN2

print(common)
