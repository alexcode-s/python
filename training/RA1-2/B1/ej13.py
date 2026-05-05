import random
# Modifica el programa anterior para que no admita dados con un número de caras impares. En el caso
# de meter un número impar de caras el programa debería de informarnos de que es erróneo y volver
# a preguntarnos por este dato.

ndice = int(input("Número de dados: "))
sides = int(input("Número de caras: "))
results = []

while sides % 2 != 0:
    sides = int(input("Número impar no válido, inténtelo de nuevo: "))

for i in range(ndice):
    results.append(random.randint(1, sides))

print(results)