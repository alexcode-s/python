ok = False

while not ok:
    ok = True
    fraccion = input('Escribe tu fracción: ')

    barras = fraccion.count('/')
    numDen = fraccion.split('/')
    numerador = numDen[0]
    denominador = numDen[1]

    if numerador.count('.') > 0 or denominador.count('.') > 0:
        ok = False
        print('Error. No puede haber decimales')

    if numerador.isalpha() or denominador.isalpha():
        ok = False
        print('Error. no puede haber letras')

    if denominador == '0':
        ok = False
        print('Error. El denominador no puede ser 0')

    if barras != 1:
        ok = False
        print('Error. No puede haber más de una barra')

    if fraccion.startswith('/') or fraccion.endswith('/'):
        ok = False
        print('Error. La fracción no puede empezar ni terminar con /')

n = int(numerador)
d = int(denominador)
resultado = n / d
redondeado = round(resultado, 3)
print('Solución:', redondeado)

