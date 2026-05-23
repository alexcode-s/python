import re
# Las matrículas españolas constan de un número de cuatro dígitos y tres letras cualesquiera en mayúsculas
# a excepción de las vocales, la Ñ y la Q. Se debe escribir un programa que detecte si una matrícula
# introducida por teclado es válida o no

matr = input("Matrícula: ")
pattern = r"^\d{4}(?!q|Q|ñ|Ñ)[A-Za-z]{3}$"

print("Matrícula válida" if re.fullmatch(pattern, matr) else "Matrícula no válida")
