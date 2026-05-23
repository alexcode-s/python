cadena = input('Escribe un texto: ')
vocales = ['a','e','i','o','u']
numVocales = 0
espaciosBlanco = cadena.count(' ')
cadena = cadena.replace(' ','')

for i in range(len(vocales)):
    vocal = vocales[i]
    if vocal in cadena:
        numVocales += cadena.count(vocal)
        cadena = cadena.replace(vocal,'')
print(f'Sin vocales ni espacios: {cadena}')
print(f'Vocales suprimidas: {numVocales}')
print(f'Espacios suprimidos: {espaciosBlanco}')