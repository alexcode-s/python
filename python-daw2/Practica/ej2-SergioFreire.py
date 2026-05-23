import random


n1 = random.randint(1,6)
n2 = random.randint(1,6)
intentos = 0

while n1 != n2:
    print(n1,'-',n2)
    intentos += 1
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)

if intentos == 0:
    print('He tenido que lanzar los dados 1 vez para que todos sean iguales')
else:
    print(f'He tenido que lanzar los dados {intentos} veces para que todos sean iguales')