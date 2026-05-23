# Solicitar una nota entre el 1 y el 10 (sin decimales) y devolver la calificación según la siguiente escala:
# 1-2 Muy deficiente, 3-4 Insuficiente, 5 Suficiente, 6 Bien, 7-8 Notable, 9-10 Sobresaliente.

n = int(input("Nota: "))
cal = None

match n:
    case 1 | 2:
        cal = "Muy deficiente"
    case 3 | 4:
        cal = "Insuficiente"
    case 5:
        cal = "Suficiente"
    case 6:
        cal = "Bien"
    case 7 | 8:
        cal = "Notable"
    case 9 | 10:
        cal = "Sobresaliente"
    case _:
        cal = None

if cal is not None:
    print(f"La calificación es: {cal}")
else:
    print("Error: la nota debe estar entre 1 y 10")
