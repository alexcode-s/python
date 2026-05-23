import re
# Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por un espacio. A continuación un
# espacio y la fecha de caducidad en formato MM/YY. El mes tiene que ser válido (entre 01 y 12)

card = input("Tarjeta de crédito: ")
pattern = r"^(\d{4} ){3}\d{4} (0[1-9]|1[0-2])/\d{2}$"

print("Tarjeta válida" if re.fullmatch(pattern, card) else "Tarjeta no válida")