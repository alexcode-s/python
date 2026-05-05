import random
# Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una lotería primitiva).
# En este ejercicio se permiten números repetidos

for i in range(6):
    print(random.randint(1, 49), end=' ')