import random
# Modifica el programa anterior para que se muestren todos los intentos que se necesiten pero que cuando se acierte
# informe de cuántas veces se ha fallado antes de lograrlo.

attempts = 0
n = random.randint(1,50)
print(f"DEBUG: {n}")
inp = -1

while inp != n and attempts < 5:
    attempts += 1
    inp = int(input("Adivine el número: "))

    if inp < n:
        print("El número secreto es mayor que el introducido.")

    if inp > n:
        print("El número secreto es menor que el introducido.")

    if inp == n:
        print("Número correcto.")

    if attempts == 5 and inp != n:
        print("Número máximo de intentos alcanzado.")