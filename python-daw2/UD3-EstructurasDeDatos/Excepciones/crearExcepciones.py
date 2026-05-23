ok = False
while not ok:
    try:
        numero = int(input('Introduce un número entero y positivo:'))
        resultado = 10 / numero
        assert numero >= 0,'No se admiten valores negativos' # Se evalúa como False
        print(resultado)
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    except ValueError:
        print('No se puede operar con letras')
    except:
        print('Hubo una excepción')
    else:  # Opcional. Se ejecuta si no ocurre ninguna excepción
        print('Todo bien')
        ok = True
    print('Programa finalizado')
