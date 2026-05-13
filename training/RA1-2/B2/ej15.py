import random
# Modificar el programa anterior para que al inciar el programa, pida 2 parámetros con el objetivo de cambiar
# la dificultad del juego: el número máximo o el número de intentos posibles.

attempts = 0
LIMIT = 5
RAND = 50
n = random.randint(1,RAND)
print(f"DEBUG: {n}")
inp = -1

while inp != n and attempts < LIMIT:
    if attempts == 0:
        RAND = int(input("Número aleatorio máximo: "))
        LIMIT = int(input("Número máximo de intentos: "))
    attempts += 1
    inp = int(input("Adivine el número: "))

    if inp < n:
        print("El número secreto es mayor que el introducido.")
    elif inp > n:
        print("El número secreto es menor que el introducido.")
    else:
        print("Número correcto.")

    if attempts == 5 and inp != n:
        print("Número máximo de intentos alcanzado.")

    if attempts == 5 or inp == n:
        again = input("¿Jugar de nuevo ? s/n: ")
        if again == "s":
            n = random.randint(1,RAND)
            print(f"DEBUG: {n}")
            attempts = 0
            inp = -1