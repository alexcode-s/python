# Programa que pida por teclado primero una cadena y luego un caracter. A continuación debe imprimir cuántas veces
# aparece dicho caracter y en las posiciones de la cadena donde lo hace.

cad = input("Cadena: ").lower()
car = input("Caracter: ").strip().lower()
reps = 0
pos = 0

if car in cad:
    reps = cad.count(car)
    pos = [i for i, c in enumerate(cad) if c == car]

    print(f"El caracter {car} se repite: {reps} veces")
    print(f"El caracter {car} se encuentra en las posiciones: {pos}")

