import random

class Cliente():
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    def mostrar(self):
        print(f"{self._dni} - {self._apellido}, {self._nombre}")

clientes = []

try:
    with open("datos.txt","r") as file, open("datosBarajados.txt", "w") as file2:
        content = file.readlines()
        nombres = []
        apellidos = []
        dnis = []
        for line in content:
            elements = line.split(" ")
            nombres.append(elements[0])
            apellidos.append(elements[1])
            dnis.append(elements[2].strip())
            cliente = Cliente(elements[0], elements[1] ,elements[2].strip())
            clientes.append(cliente)

        random.shuffle(nombres)
        random.shuffle(dnis)

        for nombre, apellido, dni in zip(nombres, apellidos, dnis):
            file2.write(f"{nombre} {apellido} {dni}\n")

except:
    print("Error con el fichero")

print("------------------------------OBJETOS------------------------------")
for c in clientes:
    c.mostrar()