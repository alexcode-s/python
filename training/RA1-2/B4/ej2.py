# Programa que reciba un número por teclado y calcule tantos números de la sucesión de Fibonacci como indique ese
# número.

n = int(input("Número: "))
fib = []
a, b = 0, 1

for _ in range(n):
    fib.append(a)
    a, b = b, a+b

print(fib)
