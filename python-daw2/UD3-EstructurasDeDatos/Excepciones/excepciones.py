ok = False
while not ok:
    try:
        numero = int(input('Introduce un número:'))
        resultado = 10 / numero
        print(resultado)
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    except ValueError:
        print('No se puede operar con letras')
    else:  # Opcional. Se ejecuta si no ocurre ninguna excepción
        print('Todo bien')
        ok = True
    print('Programa finalizado')

