import re

class Cuenta():
    def __init__(self, pais, dc, entidad, sucursal, dcCuenta, numCuenta):
        self._pais = pais
        self._dc = dc
        self._entidad = entidad
        self._sucursal = sucursal
        self._dcCuenta = dcCuenta
        self._numCuenta = numCuenta

    def mostrar(self):
        print(f"País: {self._pais}")
        print(f"DC: {self._dc}")
        print(f"Entidad: {self._entidad}")
        print(f"Sucursal: {self._sucursal}")
        print(f"DC cuenta: {self._dcCuenta}")
        print(f"Número de cuenta: {self._numCuenta}")
        print()

def valid(file_name):
    pattern = r"^([A-Z]{2})\s*((?:[0-9]\s*){2})((?:[0-9]\s*){4})((?:[0-9]\s*){4})((?:[0-9]\s*){2})((?:[0-9]\s*){10})$"

    correctos = 0
    incorrectos = 0
    try:
        with open(file_name, "r") as file:
            print(f"Códigos correctos en el fichero {file_name}:")
            for line in file:
                line = line.strip()

                match = re.fullmatch(pattern, line)

                if match:
                    correctos += 1
                    cuenta = Cuenta(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6))
                    cuenta.mostrar()
                else:
                    incorrectos += 1

            print(f"Hay {correctos} códigos correctos y {incorrectos} incorrectos")
    except:
        print("Error al abrir el archivo")


valid("cuentas.txt")