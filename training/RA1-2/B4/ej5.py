# Programa que diga si un número dado es capicúa

n = input("Número: ")
print("Es capicúa" if n == n[::-1] else "No es capicúa")
