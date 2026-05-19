import math
# Programa que calcule la primera pareja de primos gemelos por encima del 50.

def is_prime(n):
    if n < 2:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if i > 0:
            if n % i == 0:
                return False
    return True

for num in range(50, 100):
    if is_prime(num) and is_prime(num+2):
        print(f"{num} - {num+2} (gemelos)")