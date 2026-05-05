import random
# Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar quince números aleatorios entre
# el 1 y el 3. Los resultados válidos son 1, X o 2, así que si aparece un 3, se debe imprimir una X.

for i in range(15):
    n = random.randint(1, 3)
    if n == 1:
        print(f"[-1-][x][2]")
    elif n == 2:
        print(f"[1][x][-2-]")
    else:
        print(f"[1][-x-][2]")