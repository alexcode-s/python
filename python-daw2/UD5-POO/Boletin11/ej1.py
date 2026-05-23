import random


class Pokemon:
    def __init__(self, code, name, evolution=None):
        self.__code = code
        self.__name = name
        self.__evolution = evolution
        self.__pv = random.randint(50,100)

    def show(self):
       print(f'''
Código: {self.__code}
Nombre: {self.__name}
Evolución: {self.__evolution}
Puntos de vida: {self.__pv}
---------------------------------
        ''')

    def ev(self):
        if self.__evolution == None:
            evo = self
            print('Este pokemon no sabe evolucionar')
            return self
        else:
            evo = self.__evolution
        return evo

    def combateContra(self, contrincante):
        #if contrincante.__pv > 0 and self.__pv > 0:


        danio = random.randint(25,75)
        contrincante.__pv -= danio
        if contrincante.__pv <= 0:
            print(contrincante.__nombre, 'ha sido derrotado')
        else:
            danio = random.randint(25, 75)
            self.__pv -= danio
            if self.__pv <= 0:
                print(self.__name, 'ha sido derrotado')
            else:
                print('Ninguno de los Pokemons ha vencido')

p3 = Pokemon(3, "Yvisaur")
p2 = Pokemon(2, "Venasaur", p3)
p1 = Pokemon(1, "Bulbasur", p2)

p1.show()
p2.show()
p3.show()

p1 = p1.ev()
p3 = p3.ev()

p1.show()
p2.show()