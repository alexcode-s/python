from abc import abstractmethod

class Abstracta():
    def metodoNormal(self):
        print('Hola mundo')

    @abstractmethod
    def metodoAbstracto(self):
        pass

class Hija(Abstracta):
    def metodoAbstracto(self):
        print('Adios mundo')

elemento = Hija()
elemento.metodoNormal()
elemento.metodoAbstracto()

profesores = ["José María", "Natalia", "Agustín"]
iterador = iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador, "STOP"))

class diasSemana():
    def __init__(self, dia = 0):
        self.dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        self.dia = dia

    def __iter__(self):
        return self

    def __next__(self, stop=None):
        dia_actual = self.dias[self.dia]
        if self.dia == 6:
            self.dia = 0
        else:
            self.dia += 1
        return dia_actual

semana = diasSemana(1)
iterador = iter(semana)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))