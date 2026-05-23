import pickle
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

persona1 = Persona('Sergio')
persona2 = Persona('Kiara')

try:
    fichero = open('quijote.bin', 'wb')
    #pickle.dump(persona1, fichero)
    #pickle.dump(persona2, fichero)
    lista = []
    lista.append(persona1)
    lista.append(persona2)
    pickle.dump(lista, fichero)

    fichero.close()

    # Lectura
    fichero2 = open('quijote.bin', 'rb')
    l = pickle.load(fichero2)

    for elemento in l:
        print(elemento.nombre)

    fichero2.close()
except:
    print('Error al manipular el fichero')