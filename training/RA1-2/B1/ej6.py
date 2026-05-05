# Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o no

n = int(input("Número: "))

if n % 3 == 0:
    print(f"{n} es divisible por 3")
else:
    print(f"{n} no es divisibile por 3")