# Programa que pida una frase por teclado y luego la imprima separando todos los caracteres de sus palabras
# (excepto los espacios) con un guión.

cad = input("Cadena: ")
print(" ".join("-".join(c) for c in cad.split()))