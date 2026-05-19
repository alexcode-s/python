# Programa que pida una cadena por teclado y luego imprima sólo las cifras que aparecen en ella.

cad = input("Cadena: ")

digits = [c for c in cad if c.isdigit()]

print(digits)