# Incluir al ejercicio anterior operaciones adicionales: raíz cuadrada, cuadrado, cubo.

opts = ["RC", "C", "CUB"]
opt = input("Operación (S/R/M/D/RC/C/CUB): ").strip().upper()
n1 = int(input("Número 1: "))

if opt not in opts:
    n2 = int(input("Número 2: "))

match opt:
    case "S":
        print(f"{n1} + {n2} = {n1 + n2}")
    case "R":
        print(f"{n1} - {n2} = {n1 - n2}")
    case "M":
        print(f"{n1} * {n2} = {n1 * n2}")
    case "D":
        print(f"{n1} / {n2} = {n1 / n2}")
    case "RC":
        print(f"{n1 ** 0.5}")
    case "C":
        print(f"{n1 * n1}")
    case "CUB":
        print(f"{n1 ** 3}")
    case _:
        print(f"Opción no válida")