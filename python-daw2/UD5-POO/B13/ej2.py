from abc import ABC, abstractmethod
from datetime import datetime

class Vehiculo(ABC):
    def __init__(self, matricula, anioVenta, conductor, tipoSeguro):
        if anioVenta > datetime.today().year:
            raise ValueError('El año de compra no puede ser posterior al año actual')
        self._matricula = matricula
        self._anioVenta = anioVenta
        self._conductor = conductor
        self._tipoSeguro = tipoSeguro

    def anioActual(self):
        return datetime.today().year

    def antiguedadCarnet(self):
        return self.anioActual() - self._conductor.anioCarnet()

    def antiguedadVenta(self):
        return self.anioActual() - self._anioVenta + 1

    def edad(self):
        return self.anioActual() - self._conductor.anioNacimiento()

    def puntos(self):
        return self._conductor.puntos()

    @abstractmethod
    def precioSeguro(self):
        pass

class Coche(Vehiculo):
    def __init__(self, matricula, anioVenta, conductor, tipoSeguro):
        super().__init__(matricula, anioVenta, conductor, tipoSeguro)

    def precioSeguro(self):
        precio = 0

        if self._tipoSeguro == 'Terceros':
            precio = 250
        else:
            antig = self.antiguedadVenta()
            if antig == 1:
                precio = 400
            elif antig == 2:
                precio = 500
            elif antig == 3:
                precio = 700
            else:
                precio = antig * 250

        if self.puntos() < 8:
            precio += 100

        if self._tipoSeguro == 'Terceros':
            if self.edad() < 24:
                precio += 50
            if self.antiguedadCarnet() < 2:
                precio += 75

        return precio

class Moto(Vehiculo):
    def __init__(self, matricula, anioVenta, conductor, tipoSeguro):
        if tipoSeguro == 'Todo riesgo':
            raise ValueError('No se admite seguro a todo riesgo para motos')
        super().__init__(matricula, anioVenta, conductor, tipoSeguro)

    def precioSeguro(self):
        precio = 200

        if self.puntos() < 8:
            precio += 150
        if self.edad() < 24:
            precio += 25
        if self.antiguedadCarnet() < 2:
            precio += 50

        return precio

class Conductor():
    def __init__(self, nombre, nif, anioNacimiento, anioCarnet, puntosCarnet):
        self._nombre = nombre
        self._nif  = nif
        self._anioNacimiento = anioNacimiento
        self._anioCarnet = anioCarnet
        self._puntosCarnet = puntosCarnet

    def anioNacimiento(self):
        return self._anioNacimiento

    def anioCarnet(self):
        return self._anioCarnet

    def puntos(self):
        return self._puntosCarnet

