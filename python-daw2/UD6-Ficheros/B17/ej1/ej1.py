def compararFicheros(f1, f2):
    return f1 == f2

try:
    f1 = open('quijote.txt', 'r+')
    f1.write('Hola mundo\n')
    f1.seek(0)
    file1 = f1.read()

    f2 = open('quijote2.txt', 'r+')
    f2.write('Hola mundo\n')
    f2.seek(0)
    file2 = f2.read()

    f1.close()
    f2.close()

    match = compararFicheros(file1, file2)
    if match:
        print('Los ficheros son iguales')
    else:
        print('Los ficheros no son iguales')
except:
    print('Error al abrir el fichero')

