import random

n1 = int(input('Número aleatorio desde: '))
n2 = int(input('Hasta: '))

if n1 < n2:
    print(random.randint(n1,n2))
if n1 > n2:
    print(random.randint(n2,n1))
