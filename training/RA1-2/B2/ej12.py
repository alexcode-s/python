import random
# Programar un juego en el que se deba acertar un número entre el 1 y el 50 que el ordenador ha elegido de forma
# aleatoria. El programa indicará si se ha acertado, si se ha superado el número o si está por encima del
# introducido. El programa finaliza cuando se acierta o cuando se supera el número máximo de intentos establecidos
# en 5.

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