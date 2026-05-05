import random
# Modificar el programa anterior para que si el primer número ingresado es mayor que el segundo
# funcione correctamente.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
rn = random.randint(n1, n2) if n1 < n2 else random.randint(n2, n1)

print(rn)