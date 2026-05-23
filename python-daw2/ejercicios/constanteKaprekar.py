def Order(n, orden):
    numCadena = str(n)
    numLista = list(numCadena)
    numLista.sort(reverse = orden)
    numListaCadena = "".join(numLista)
    return int(numListaCadena)

ok = False
while not ok:
    try:
        n1 = int(input('Introduzca un número de exactamente 4 cifras: '))
        assert len(set(str(n1))) == 4, 'El número debe tener exactamente 4 cifras'
    except:
        print('Hubo una excepción')
    else:
        print('Correcto')
        ok = True
        result = 0
        cont = 1

        while result != 6174:
            numDesc = Order(n1, True)
            numAsc = Order(n1, False)
            result = numDesc - numAsc
            print(f'{numDesc} - {numAsc} = {result}')
            n1 = result
            if result != 6174: cont += 1
        print(f'Constante de Kaprekar obtenida en {cont} operaciones')