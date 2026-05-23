
try:
    # Abrir fichero
    fichero = open('quijote.txt') # Por defecto abre el fichero en modo lectura (open('quijote.txt', 'rt'))

    # ------------------ READ ------------------
    # Variable con el contenido del fichero
    #texto = fichero.read()
    #print(texto)

    # ------------------ READLINES ------------------
    # Variable con el contenido del fichero en una lista
    # Si la lectura anterior no estuviera comentada, el cursor estaría al final del contenido, por lo que devolvería una lista vacía
    #texto2 = fichero.readlines()
    #print(texto2)

    # ------------------ READLINE ------------------
    linea = fichero.readline()
    while linea!="":
        if linea[-1] == '\n': # Comprobar si el último caracter es \n
            print(linea[:-1])
        else:
            print(linea)
        linea = fichero.readline()

    # Cerrar fichero
    fichero.close()
except:
    print('Error al manipular el fichero')
