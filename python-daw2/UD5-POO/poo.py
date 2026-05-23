# Se pueden modificar atributos de un objeto desde fuera
# No se puede proteger un metodo
# No se puede sobrecargar atributos y métodos (ya lo están de por sí)

# Definir clase
class CuentaCorriente:
    # Variable equivalente a variable global
    __numCuentas = 0
    # Definir constructor (es una función, como en Java)
    # Nota: Funciones mágicas
    # self equivalente a this de JavaScript
    def __init__(self, code, holder, balance=500):
        self.__code = code
        self.__holder = holder
        self.__balance = balance
        CuentaCorriente.__numCuentas += 1

    def __add__(self, segundaCuenta):
        self.__balance += segundaCuenta.__balance
        self.__holder += segundaCuenta.__holder
        return self

    '''
    # Getters y Setters de manera tradicional
    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance
    '''

    # Decoradores (anotaciones en Java).
    # Sirve para interactuar con los atributos de la clase
    @classmethod
    def getNumCuentas(cls):
        return (cls.getNumCuentas())

    # Métodos auxiliares. Pertenece a la clase pero no puede manipular ningún objeto de la clase.
    @staticmethod
    def devolverDatosSucursal():
        print('Calle del Pez, 7. 28032, Madrid')

    # Definir función que se comportará como atributo (Getter)
    @property
    def balance(self):
        return self.__balance

    # Definir setter de la misma manera (siempre después del getter)
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        data = str(self.__code)+' - '+self.__holder+' - '+str(self.__balance)
        return data
# Construir objetos
c1 = CuentaCorriente(1234, 'Sergio Freire', 100000000)
c2 = CuentaCorriente(4321, 'Kerin Aguilera', 500000)

# Modificar atributos de la clase
c2.balance = 600000
print(c2.balance)

# print(CuentaCorriente.__numCuentas)

# Llamar al metodo auxiliar
c2.devolverDatosSucursal()

'''
Variables privadas y protegidas, convención:
_code -> protected
__balance -> private
'''
# Acceder a atributo property
print(c2.balance)

# Tipo de dato adicional
class Alumno:
    pass

alumno1 = Alumno()
alumno1.nombre = 'Sergio'
alumno1.apellidos = 'Freire'
alumno1.edad = 22
alumno1.telefono = '645734512'

# Metodos dunder / metodos mágicos
'''
__del__ -> Destructor de un objeto
__str__ ->
__len__ ->

# Aritméticos
__add__
__sum__
__mult__
__truediv__

# Lógicos
__eq__
__ne__
__gt__
__lt__

__iter__
__next__
'''

print(str(c1))