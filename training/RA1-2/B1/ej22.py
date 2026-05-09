import random
# Programa que genere un número primo aleatorio entre el 10.000.000 y el 50.000.000

n = random.randint(10000000, 50000000)
prime = not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))

while not prime:
    n = random.randint(10000000, 50000000)
    prime = not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1))

print(n)