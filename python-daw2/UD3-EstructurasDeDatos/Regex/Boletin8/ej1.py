import re

# Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28
# Ejemplo: 28032

pattern = r"^28\d{3}$"

n = "28017"

if re.fullmatch(pattern, n):
    print('Coincidencia')
else:
    print('No coincide')