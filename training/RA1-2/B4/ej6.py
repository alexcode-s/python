import math
# Programa que muestre por pantalla los 50 primeros números primos, sus raíces cuadradas, sus cuadrados y sus cubos.

def is_prime(n):
    if n < 2:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if i > 0:
            if n % i == 0:
                return False
    return True

for num in range(50):
    if is_prime(num):
        print(num)


