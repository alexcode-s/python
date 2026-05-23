import re

# El primer caracter será del 6-8 (incluidos), los siguientes {9} restantes podrán ser del 0-9
patron = r"[6-8][0-9]{8}"

# Validar
n1 = '655112233'
n2 = '9613344555'

# Con match
print('Match')
if re.match(patron, n1):
    print(f'{n1} es un teléfono móvil')
else:
    print(f'{n1} no es un teléfono móvil')

if re.match(patron, n2):
    print(f'{n2} es un teléfono móvil')
else:
    print(f'{n2} no es un teléfono móvil')
print('--------------------------------------')
# Con search
print('Search')
if re.search(patron, n1):
    print(f'{n1} es un teléfono móvil')
else:
    print(f'{n1} no es un teléfono móvil')

if re.search(patron, n2):
    print(f'{n2} es un teléfono móvil')
else:
    print(f'{n2} no es un teléfono móvil')

print('--------------------------------------')
# Con fullmatch
print('Fullmatch')
if re.fullmatch(patron, n1):
    print(f'{n1} es un teléfono móvil')
else:
    print(f'{n1} no es un teléfono móvil')

if re.fullmatch(patron, n2):
    print(f'{n2} es un teléfono móvil')
else:
    print(f'{n2} no es un teléfono móvil')
print('--------------------------------------')

patron2 = r'[0-9]{4}[\s|-]?[B-DF-HJL-NPR-TV-Z]{3}'
patron3 = r"[^579]"
patron4 = r'^[A-Z]{3}$'