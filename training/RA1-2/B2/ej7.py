# Programa que pida un número por teclado e imprima la tabla de
# multiplicar de dicho número del 1 al 10.

n = int(input("Número: "))

for i in range(11): print(f"{n} x {i} = {n*i}")