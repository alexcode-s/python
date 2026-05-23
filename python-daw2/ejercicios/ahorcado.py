frase = input('Introduce una frase: ')
letra = input('Letra a mantener: ')

for i in frase:
    if i == letra:
        print(i,end='')
    elif i == ' ':
        print(' ',end='')
    else:
        print('*',end='')