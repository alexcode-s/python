import re
# Programa que reciba por teclado una fecha en formato DD/MM/YYYY. El programa debe comprobar si la fecha es
# correcta teniendo en cuenta:
# - Que el formato sea correcto
# - Que la fecha sea totalmente válida teniendo en cuenta incluso los años que
#   son bisiestos (aquellos divisibles entre 4)

dt = input("Fecha: ").strip()
match = re.fullmatch(r"^(\d{2})/(\d{2})/(\d{4})$", dt)

if match:
    d, m, y = map(int, match.groups())
    if y % 4 == 0:
        print("Fecha válida" if d <= 29 and m == 2 else "Fecha no válida - Año bisiesto")
    else:
        print("Fecha válida" if 0 < d <= 31 and 1 <= m <= 12 else "Fecha no válida")
else:
    print("Fecha no válida")