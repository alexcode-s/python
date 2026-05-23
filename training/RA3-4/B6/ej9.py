import re
# Validar un número de 4 cifras mínimo y 8 cifras máximo

n = input("Número: ")
pattern = r"\d{4,8}"

print("Número válido" if re.fullmatch(pattern, n) else "Número no válido")
