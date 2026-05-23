coincide = False
intentos = 0
passwd1 = input('Introduzca una contraseña: ')
passwd2 = input('Repita la contraseña: ')

if passwd1 == passwd2:
    coincide = True
    print('Contraseña guardada')
    print('A la primera!')
else:
    intentos += 1

while not coincide:
    print('Las contraseñas no coinciden. Inténtelo de nuevo')
    passwd1 = input('Introduzca una contraseña: ')
    passwd2 = input('Repita la contraseña: ')
    intentos += 1
    if passwd1 == passwd2:
        coincide = True
        print('Contraseña guardada')
        print(f'Intentos {intentos}')