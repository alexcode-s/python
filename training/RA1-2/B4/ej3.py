# Programa que reciba un número por teclado y muestre en orden todos los números de la sucesión de Fibonacci que sean
# menores o iguales al enviado como argumento.

n = int(input("Número: "))
fib = []
a, b = 0, 1

while a <= n:
    fib.append(a)
    a, b = b, a+b

print(fib)