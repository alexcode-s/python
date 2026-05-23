import random

# Ejercicio 16
nums = []

for i in range(6):
    nums.append(random.randint(1,49))
print(nums)

# Ejercicio 17
for i in range(15):
    numeros = [0]*3
    numeros[0] = random.randint(1,3)
    numeros[1] = random.randint(1, 3)
    numeros[2] = random.randint(1, 3)

    for i in range(len(numeros)):
        if numeros[i] == 3:
            print('x',end=" ")
        else:
            print(i,end=" ")
    print()

# Ejercicio 18
apocalipsis = random.randint(1,1000)
dias = 0
if apocalipsis == 666:
    print(apocalipsis,'- El día ha llegado')

while apocalipsis != 666:
    apocalipsis = random.randint(1,1000)
    if apocalipsis != 666:
        dias+=1
        print(apocalipsis)
    else:
        print(apocalipsis)
        print('Días para el fin del mundo:',(666-dias))

# Ejercicio 19
numero = int(input('Comprobar divisores del número: '))
print('Divisores: ')
for i in range(numero,0,-1):
    if numero%i == 0:
        print(i)

