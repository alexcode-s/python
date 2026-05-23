import re
# Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco. Las palabras no pueden contener
# números y deben empezar ambas por una letra mayúscula

cad = input("Dos palabras separadas por un único espacio en blanco: ")
pattern = r"^[A-Z][A-za-z]* [A-Z]+[A-za-z]*"

print("Cadena válida" if re.fullmatch(pattern, cad) else "Cadena no válida")