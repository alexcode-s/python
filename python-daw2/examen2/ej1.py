def cifrarLinea(n):
    listaX = []
    x = 10 - n
    for i in range(x):
        listaX.append('X')

    for i in range(n):
        listaX.append('0')

    return tuple(listaX)

pin = int(input('Introduzca el pin: '))
pinList = list(str(pin))

for i in pinList:
    lineaCifrada = (cifrarLinea(int(i)))
    strCifrado = str(lineaCifrada).replace('(',"").replace(')','').replace(',','')
    print(strCifrado)