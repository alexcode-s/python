import random
# Programa que genere números aleatorios entre el 1 y el 100 sin para y que solo se detenga cuando salga el 666.
# Al llegar al 666, el programa debería indicarlo mediante un mensaje mostrando el número.

n = random.randint(1, 1000)
count = 1

while n != 666:
    print(n)
    n = random.randint(1, 1000)
    count += 1

print(n)