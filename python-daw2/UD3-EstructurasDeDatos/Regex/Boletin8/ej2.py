import re


# Empiezan por 9
# Tiene 7 dígitos más
# Entre los dígitos puede hacer espacios o guiones opcionales
# Longitud total flexible por los separadores, pero 8 digitos en total
pattern = r'^9(?:[- ]?\d){7}$'
n = (input('Número de teléfono: '))

if re.fullmatch(pattern, n):
    print('Número aceptado')
else:
    print('Número no acept'
          'ado')