import re
# Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28. Ejemplo: 28032

cod = input("Código postal: ")
pattern = r"^28\d{3}$"

print("Código postal válido" if re.fullmatch(pattern, cod) else "Código postal no válido")