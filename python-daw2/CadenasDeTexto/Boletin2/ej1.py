# Ejercicio 1
ls = [0]*3

'''
ls[0] = input('Palabra 1: ')
ls[1] = input('Palabra 2: ')
ls[2] = input('Palabra 3: ')
'''
ls[0] = 'Hola'
ls[1] = 'Mundo'
ls[2] = 'Cruel'

ls.sort()
print(ls)

# Ejercicio 2
ls.reverse()
print(ls)
'''
# Ejercicio 3
n = float(input('Introduzca el precio: '))
iva = n * 0.21
precioFinal = n + iva
input(round(precioFinal,2))
'''
'''
# Ejercicio 4
notas = [0]*2
for i in range(len(notas)):
    notas[i] = float(input(f'Nota {i+1}: '))
    while notas[i]

suma = notas[0] + notas[1]
media = suma / 2
input(round(media))
'''
# Ejercicio 5
nts = [0]*3
totales = [0]*len(nts)

for i in range(len(nts)):
    nts[i] = input(f'Nota {i+1}: ')
    while not isinstance(nts[i],(int, float)):
        nts[i] = input(f'Valor no válido para la nota {i+1}: ')

totales[0] = nts[0] * 0.05
totales[1] = nts[1] * 0.15
totales[2] = nts[2] * 0.8

notaFinal = 0
for i in range(len(nts)):
    notaFinal += totales[i]

input(f'Nota final real: {notaFinal}')
input(f'Nota final de boletín: {round(notaFinal)}')
