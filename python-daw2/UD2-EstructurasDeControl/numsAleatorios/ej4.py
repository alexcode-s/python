fraccion = input('Escribe tu fracción: ')
barras = fraccion.count('/')
numDen = fraccion.split('/')
numerador = numDen[0]
denominador = numDen[1]
decimales = True if numerador.count('.') or denominador.count('.') else False
caracteres = True if numerador.isalpha() or denominador.isalpha() else False
cero = True if denominador == '0' else False
errorBarras = True if barras > 1 or barras < 1 else False
errorIndexBarra = True if fraccion.startswith('/') or fraccion.endswith('/') else False
errorNumDen = True if decimales or caracteres else False

while decimales or caracteres or cero or errorBarras or errorIndexBarra or errorNumDen:
    fraccion = input('Error, escribe tu fracción de nuevo: ')
    barras = fraccion.count('/')
    numDen = fraccion.split('/')
    numerador = numDen[0]
    denominador = numDen[1]
    decimales = True if numerador.count('.') or denominador.count('.') else False
    caracteres = True if numerador.isalpha() or denominador.isalpha() else False
    cero = True if denominador == '0' else False
    errorBarras = True if barras > 1 or barras < 1 else False
    errorIndexBarra = True if fraccion.startswith('/') or fraccion.endswith('/') else False
    errorNumDen = True if decimales or caracteres else False

n = int(numerador)
d = int(denominador)
resultado = n/d
redondeado = round(resultado,3)
print('Solución:',redondeado)

