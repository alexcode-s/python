import random

numeros = list()
num = int(input('Números aleatorios entre el 1 y el: '))
n = 0

for i in range(5):
    n = random.randint(1,num)
    while n % 2 != 0:
        n = random.randint(1,num)
    numeros.append(n)

for i in range(len(numeros)):
    cont = numeros.count(numeros[i])
    while cont > 1:
        numeros.remove(numeros[i])
        n = random.randint(1,num)
        while n % 2 != 0:
            n = random.randint(1, num)
        numeros.append(n)
        cont = numeros.count(numeros[i])
print(numeros)


