import random
# Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
# comprendido entre ambos. Por el momento no es relevante que el primer número siempre
# deba ser menor que el segundo, simplemente no se debe meter en un orden incorrecto.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

rn = random.randint(n1, n2)
print(rn)