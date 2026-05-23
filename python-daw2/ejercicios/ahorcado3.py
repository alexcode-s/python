frase = input('Introduce una frase: ')
acertado = False
intentos = 0
frase2 = ''

for _ in range(len(frase)):
    frase2 += '*'
print(frase2)

while not acertado:
    letra = input('Introduce una letra: ')
    apariciones = frase.count(letra)

    if apariciones > 0 and not acertado:
        frase3 = ''
        intentos += 1
        print(f'La letra {letra} aparece en {apariciones} ocasiones')
        for i in range(len(frase)):
            if frase[i] == letra:
                frase3 += frase[i]
            else:
                frase3 += frase2[i]
        frase2 = frase3
        print(frase2)
    else:
        intentos += 1
        print(f'La letra {letra} aparece en 0 ocasiones')

    if frase == frase2:
        acertado = True
print(f'Has ganado. Has necesitado {intentos} intentos para completar la frase')




