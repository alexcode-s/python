import re
# Validar una clave con el siguiente formato: XX00-xxX-00. Donde las X deben ser letras mayúsculas, las x letras
# minúsculas y los 0 dígitos.

key = input("Clave: ")
pattern = r"^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$"

print("Formato válido" if re.fullmatch(pattern, key) else "Formato no válido")