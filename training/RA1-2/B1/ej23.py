import random
# Programa que escriba todos los números primos que hay entre el 1 y el 100

for i in range(100):
    if not any(i % n == 0 for n in range(2, int(i ** 0.5) + 1)):
        print(i)

