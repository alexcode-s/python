class Sucursal():
    def __init__(self, direccion, provincia, id, cc=None):
        self.__direccion = direccion
        self.__provincia = provincia
        self.__id = id
        self.__cuentas = []
        if cc:
            self.__cuentas.append(cc)

    def mostrarProvincia(self):
        return self.__provincia

    def mostrarId(self):
        return self.__id

    def mostrarCC(self):
        print(self.__cc.listarClientes())

    def mostrarIbans(self):
        print(f'Cuentas de la sucursal {self.__id} ({self.__provincia})')
        total = 0
        for account in self.__cuentas:
            account.mostrarCuentas()
            total += account.saldo()
        print(f'Saldo total: {total}')

    def agregarCuentas(self, *cc):
        for c in cc:
            self.__cuentas.append(c)

class Cliente():
    def __init__(self, nombre, apellidos, nif, tlf, sucursal):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nif = nif
        self.__tlf = tlf
        self.__sucursal = sucursal

    def listarCliente(self):
        return f'{self.__nombre} {self.__apellidos}. Cliente de la sucursal {self.__sucursal.mostrarId()} ({self.__sucursal.mostrarProvincia()}) '

class CC():
    def __init__(self, iban, saldo, titulares, sucursal):
        self.__iban = iban
        self.__saldo = saldo
        self.__titulares =  []
        self.__titulares = titulares
        self.__sucursal = sucursal

    def listarClientes(self):
        total = 0
        for titular in self.__titulares:
            print(titular.listarCliente())
            print(f'{self.__iban} - Saldo: {self.__saldo}€')
            total += self.__saldo
        print(f'Saldo total: {total}€')

    def saldo(self):
        return self.__saldo

    def mostrarCuentas(self):
        print(f'{self.__iban} - Saldo: {self.__saldo}€')

sucursal1 = Sucursal('Calle del pez', 'Madrid', '0055')
cliente1 = Cliente('Sergio', 'Freire Cuenca', '1234561','678678678', sucursal1)
cuenta1 = CC('ES68 1234 055 123456789012', 500, [cliente1], sucursal1)
cuenta2 = CC('ES68 1234 055 432187654356', 1000, [cliente1], sucursal1)

sucursal1.agregarCuentas(cuenta1, cuenta2)

cuenta1.listarClientes()
cuenta2.listarClientes()
print('-----------------------------------------------')
sucursal1.mostrarIbans()