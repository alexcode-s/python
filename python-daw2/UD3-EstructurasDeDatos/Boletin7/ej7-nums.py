import random

n = int(input('Escriba un número: '))
lista = []
media = 0

for i in range(n):
    rn = random.randint(10, 10000)
    media += rn
    lista.append(rn)

lista.sort()

print(lista)
print(f'Máximo: {lista[len(lista)-1]}')
print(f'Mínimo: {lista[0]}')
print(f'Media: {round(media/len(lista), 2)}')
