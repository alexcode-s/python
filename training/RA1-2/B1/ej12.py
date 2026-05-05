import random
# Escribir un programa que sirva como un asistente para un juego de rol. Tu programa debería pedir
# por teclado el número de dados que se van a tirar y el número de caras de estos (4,6,8,12, etc).
# A continuación debería de hacer la tirada y mostrarla.

ndice = int(input("Número de dados: "))
sides = int(input("Número de caras: "))
results = []

for i in range(ndice):
    results.append(random.randint(1, sides))

print(results)