import os
import pickle

class Empleado():
    def __init__(self, datos):
        info = datos.split(";")
        self._nombre = info[0].split(",")[1].strip()
        self._apellido = info[0].split(",")[0].strip()
        self._cargo = info[1]
        self._salario = info[2]
        self._edad = info[3]

    def mostrar(self):
        print(f"Empleado: {self._nombre} {self._apellido}")
        print(f"Cargo: {self._cargo}")
        print(f"Años hasta su jubilación ordinaria: {67 - int(self._edad)}")
        print(f"Salario neto anual: {float(self._salario) * 14}")

e = Empleado("Imedio, Demetrio;Programador Categoría 2;1599.56;34")
e.mostrar()

def grabarEmpleado(ruta, nuevo_empleado):
    lista_empleados = []

    # 1. Intentamos leer lo que ya existe
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        try:
            with open(ruta, "rb") as f:
                lista_empleados = pickle.load(f)
        except EOFError:
            # Si por algún motivo falla la lectura, empezamos de cero
            lista_empleados = []

    # 2. Añadimos el nuevo objeto a la lista
    lista_empleados.append(nuevo_empleado)

    # 3. Guardamos la lista completa (sobrescribiendo el fichero con la nueva versión)
    with open(ruta, "wb") as f:
        pickle.dump(lista_empleados, f)
    print(f"Éxito: {nuevo_empleado._nombre} guardado en el fichero binario.")

def listarEmpleados(ruta):
    if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
        print("El fichero no existe o está vacío.")
        return

    print()
    print("--- LISTADO DE EMPLEADOS GRABADOS ---")
    with open(ruta, "rb") as f:
        empleados = pickle.load(f)
        for emp in empleados:
            print(f"{emp._nombre} {emp._apellido} ({emp._edad})")

# Creamos algunos objetos de prueba con el formato del enunciado
e1 = Empleado("Imedio, Demetrio; Programador Categoría 2; 1599.56; 34")
e2 = Empleado("Borriquero, Luis Ricardo; Analista; 2500.00; 46")

ruta_archivo = "empleados.bin"

# Grabamos los empleados
grabarEmpleado(ruta_archivo, e1)
grabarEmpleado(ruta_archivo, e2)

# Mostramos el listado final leyendo del fichero
listarEmpleados(ruta_archivo)

# Opcional: Mostrar los datos calculados del ejercicio 19
print("\nDetalle del primer empleado:")
e1.mostrar()