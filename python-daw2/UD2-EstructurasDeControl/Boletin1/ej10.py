import random

n1 = random.randint(1,6)
n2 = random.randint(1,6)
intentos = 0

while n1 != n2:
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    print(n1,n2)
    intentos+=1
if n1 == n2:
    print(n1,n2)
    intentos+=1
print('Intentos:',intentos)

# Ejercicio 12 y 13
numDados = int(input('Número de dados: '))
numCaras = int(input('Número de caras: '))
if numCaras%2 == 0:
    print('Vamos a tirar',numDados,'dados de',numCaras,'caras')
    for _ in range(0,numDados):
        print(random.randint(1,numCaras))
else:
    print('Número de caras inválido')