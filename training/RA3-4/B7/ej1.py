# Programar una pequeña calculadora. Solicitar 2 números al usuario y luego que escriba la operación que quiere hacer
# (S para sumar, R para resta, M para multiplicar y D para dividir). Se debe usar match.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
opt = input("Operación (S/R/M/D): ").strip().upper()

match opt:
    case "S":
        print(f"{n1} + {n2} = {n1 + n2}")
    case "R":
        print(f"{n1} - {n2} = {n1 - n2}")
    case "M":
        print(f"{n1} * {n2} = {n1 * n2}")
    case "D":
        print(f"{n1} / {n2} = {n1 / n2}")
    case _:
        print(f"Opción no válida")
