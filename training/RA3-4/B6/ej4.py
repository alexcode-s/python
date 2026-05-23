import re
# Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido de 2 dígitos), luego un espacio
# y a continuación un número de teléfono. Ejemplo: +34 912233444

n = input("Número de teléfono con prefijo internacional: ")
pattern = r"^\+\d{2} \d{9}$"

print("Número válido" if re.fullmatch(pattern, n) else "Número no válido")
