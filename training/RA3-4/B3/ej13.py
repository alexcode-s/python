import re
# Modificar el programa anterior contemplando que entre los números y las letras podría haber un espacio
# en blanco (uno solo) o un guión. En ambos casos se considerará también que la matrícula es válida (si
# cumple también con el resto de requisitos).

matr = input("Matrícula: ")
pattern = r"^\d{4}[ -]?(?!q|Q|ñ|Ñ)[A-Za-z]{3}$"

print("Matrícula válida" if re.fullmatch(pattern, matr) else "Matrícula no válida")