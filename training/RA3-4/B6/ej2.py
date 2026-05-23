import re
# Validar un número de teléfono.

n = input("Número de teléfono: ")
pattern = r"^9\d{7}$"

print("Número de teléfono válido" if re.fullmatch(pattern, n) else "Número de teléfono no válido")
