# Herencia
# Todo lo que este definido en el hijo, tiene prioridad sobre el padre

class Padre:
    def __init__(self):
        self._title = 'Soy la clase padre'

    def show(self):
        print('PPP',self._title)

class Hijo(Padre):
    def __init__(self):
        self._title = 'Soy la clase hijo'

    def mostrar(self, mensaje):
        super().show()
        print(mensaje)

class Madre:
    def __init__(self):
        self._title = 'Soy la clase madre'

    def show(self):
        print('MMM',self._title)

o1 = Padre()
o1.show()

o2 = Hijo()
o2.mostrar('Soy la clase madre')

