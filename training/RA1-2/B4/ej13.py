# Programa que lea un número y un caracter y visualice una matriz compacta reptitiendo ese caracter y con tantas filas
# y columnas como indique el número.

n = int(input("Número: "))
c = input("Caracter: ")

for _ in range(n):
    print(c * n)
