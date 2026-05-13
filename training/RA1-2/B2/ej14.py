import random
# Modificar programa anterior para que al final del programa pida si se desea volver a jugar y en caso afirmativo
# se comience una nueva partida

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

    if attempts == 5 or inp == n:
        again = input("¿Jugar de nuevo ? s/n: ")
        if again == "s":
            n = random.randint(1,50)
            print(f"DEBUG: {n}")
            attempts = 0
            inp = -1