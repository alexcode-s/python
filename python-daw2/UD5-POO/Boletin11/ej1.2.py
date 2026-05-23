import random

class Pokemon():
    def __init__(self, code, name, type, evolution=None):
        self._code = code
        self._name = name
        self._type = type
        self._evolution = evolution
        self._pv = random.randint(50, 100)

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def pv(self):
        return self._pv

    def ev(self):
        if self._evolution == None:
            evo = self
            print('Este Pokemon no sabe evolucionar')
        else:
            evo = self._evolution
        return evo

    def combat(self, enemy):
        damage = random.randint(25, 75)
        enemy._pv -= damage

        if enemy.pv <= 0:
            print(f'Ha ganado {self._name}!')
        else:
            damage = random.randint(25, 75)
            self._pv -= damage
            if self._pv <= 0:
                print(f'Ha ganado {enemy.name}')
            else:
                print('Empate!')

    def show(self):
        print(f'Código: {self._code} | Nombre: {self._name} | Tipo: {self._type} | Evolución: {self._evolution}')

p3 = Pokemon(22, "Raichu", "Eléctrico")
p1 = Pokemon(20,"Pikachu","Eléctrico", p3)
p2 = Pokemon(21, "Charmander", "Fuego","Charmeleon")

p1.show()
p2.show()