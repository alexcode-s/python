import math

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

operacion = input('Introduzca operación: ')

match operacion:
    case 'S':
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    case 'R':
        resultado = n1 - n2
        print(f'{n1} - {n2} = {resultado}')
    case 'M':
        resultado = n1 * n2
        print(f'{n1} x {n2} = {resultado}')
    case 'D':
        resultado = n1 / n2
        print(f'{n1} / {n2} = {resultado}')
    case 'RC':
        rcn1 = math.sqrt(n1)
        rcn2 = math.sqrt(n2)
        print(f'Raíz cuadrada de {n1} = {rcn1}')
        print(f'Raíz cuadrada de {n2} = {rcn2}')
    case 'C':
        cn1 = math.pow(n1, 2)
        cn2 = math.pow(n2, 2)
        print(f'Cuadrado de {n1} = {cn1}')
        print(f'Cuadrado de {n2} = {cn2}')
    case 'CB':
        cbn1 = math.pow(n1, 3)
        cbn2 = math.pow(n2, 3)
        print(f'Cubo de {n1} = {cbn1}')
        print(f'Cubo de {n2} = {cbn2}')