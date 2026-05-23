# Programa que reciba una cadena de texto por teclado y la muestre sin vocales.

cad = input("Cadena: ").lower()
vocals = ["a", "e", "i", "o", "u"]
inv = "".join(v for v in cad if v not in vocals)
print(inv)