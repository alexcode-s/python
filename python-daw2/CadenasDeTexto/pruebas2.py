salir = False

while not salir:
    print('Opción 1')
    print('Opción 2')
    print('Opción 3')
    print('Opción 4')
    opc = int(input('Seleccione una opción: '))

    match opc:
        case 1:
            print('Número 1')
        case 2:
            print('Número 2')
        case 3:
            print('Número 3')
        case 4:
            print('Saliendo')
            salir = True
        case _:
            print('No válido')