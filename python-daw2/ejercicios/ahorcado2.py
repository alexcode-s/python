frase = input('Introduce una frase: ')
letra = input('Letra a mantener: ')

for i in frase:
    if i == letra:
        print(i,end='')
    elif i == ' ':
        print(' ',end='')
    else:
        print('*',end='')

print()
letra2 = input('Introduce una letra: ')
ap = frase.count(letra2)
print(f'La letra {letra2} aparece en {ap} ocasiones')

for i in frase:
    if i == letra or i == letra2:
        print(i,end='')
    elif i == ' ':
        print(' ',end='')
    else:
        print('*',end='')
