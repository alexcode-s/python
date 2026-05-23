import pickle

try:
    fichero = open('quijote.bin', 'rb')
    l = pickle.load(fichero)

    for elemento in l:
        print(elemento)

    fichero.close()
except:
    print('Error al manipular el fichero')