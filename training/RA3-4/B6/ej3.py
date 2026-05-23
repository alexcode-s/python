import re
# Validar un número de teléfono móvil (debe empezar por 6, 7 u 8)

n = input("Número de teléfono móvil: ")
pattern = r"^(6|7|8)\d{8}$"

print("Número válido" if re.fullmatch(pattern, n) else "Número no válido")

