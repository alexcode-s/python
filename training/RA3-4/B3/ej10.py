import re
# Programa que valide si un NIF español introducido por teclado es correcto. La longitud exacta ha de ser de 9
# caracteres. Los ocho primeros han de estar escritos en mayúsculas o minúsculas.

nif = "12345678B"
pattern = r"^\d{8}[A-Za-z]$"

print("NIF válido" if re.fullmatch(pattern, nif) else "NIF no válido")