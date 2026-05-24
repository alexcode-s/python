def ordenar_descendente(n):
    s = str(n).zfill(4)
    return int(''.join(sorted(s, reverse=True)))

def ordenar_ascendente(n):
    s = str(n).zfill(4)
    return int(''.join(sorted(s)))

def kaprekar_constant(num):
    if not isinstance(num, int) or num < 1000 or num > 9999:
        print("Error: El número debe ser un entero de cuatro cifras (1000-9999).")
        return
    if len(set(str(num))) == 1:  # Todos los dígitos iguales
        print("Error: El número no puede tener sus cuatro cifras iguales (ej. 2222).")
        return

    pasos = []
    actual = num
    operaciones = 0

    while actual != 6174:
        # Obtener el número con dígitos ordenados asc y desc
        mayor = ordenar_descendente(actual)
        menor = ordenar_ascendente(actual)
        diferencia = mayor - menor

        str_mayor = str(mayor).zfill(4)
        str_menor = str(menor).zfill(4)
        pasos.append(f"{str_mayor} – {str_menor} = {diferencia}")

        actual = diferencia
        operaciones += 1

        if operaciones > 10:
            print("Advertencia: Se excedió el número esperado de iteraciones.")
            break

    print(f"Pasos para obtener la constante de kaprekar a partir del número {num}:", " ".join(pasos))
    print(f"Constante de kaprekar obtenida con {operaciones} operaciones")
