import re
# Mejorar programa anterior para que detecte si se trata de un NIF o un NIE y comunique, además de si es válido
# de qué tipo es.

# doc = "ABDCEFGH5"
doc = "Y1234567A"
nif_pattern = r"^\d{8}[A-Za-z]$"
nie_pattern = r"^[xXyYzZ]\d{7}[A-Za-z]$"

if re.fullmatch(nif_pattern, doc):
    print("Documento válido, es un NIF")
elif re.fullmatch(nie_pattern, doc):
    print("Documento válido, es un NIE")
else:
    print("Documento no válido")
