lista = [32,67,43,76,98,12,31,11,10,54,32,22,11,22]

print('Elementos repartidos:')

for i in lista:
    n = lista.count(i)
    if n > 0:
        print(f'El número {i} aparece {n} veces')

