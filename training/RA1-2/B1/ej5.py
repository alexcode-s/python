# Escribir un programa que pida por teclado un número al usuario y diga si es par o impar

n = int(input("Número: "))

if n % 2 == 0:
    print(f"{n} es par")
else:
    print(f"{n} es impar")