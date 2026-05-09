# Programa que pida un número por teclado y calcule si es primo o no.

n = int(input("Número: "))
primo = False

if n >= 2:
     primo = not any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)) # Si encuentra uno = True

print("Primo" if primo else "No es primo")