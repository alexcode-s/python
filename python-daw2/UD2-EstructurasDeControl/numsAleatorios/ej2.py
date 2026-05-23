import random

numeros = list()
pares = 0

for i in range(10):
    n = random.randint(1,1000)
    numeros.append(n)
print(numeros)

for i in numeros:
    if i % 2 == 0:
        pares += 1
print(f'He generado {pares} números pares y {len(numeros)-pares} impares')
numeros.sort()
print(f'El número mayor ha sido el {numeros[len(numeros)-1]} y el menor el {numeros[0]}')