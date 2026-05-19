# Programa que sume por un lado las cifras pares y por otro las impares de un número y muestre ambos resultados.

num = input("Número: ")
nums = [int(d) for d in num]
pares_total = 0
impares_total = 0

for n in nums:
    if n % 2 == 0:
        pares_total += n
    else:
        impares_total += n

print(f"Suma de las cifras pares: {pares_total}")
print(f"Suma de las cifras impares: {impares_total}")