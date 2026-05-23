# Programa o una función que reciba un diccionario con los datos de los clientes de una tienda y su edad y los muestre
# por consola ordenados por nombre de pila. El diccionario debe estar creado en el código.

def mostrar_clientes(c):
    cls = []
    for name, age in c.items():
        surname, name = name.split(", ")
        cls.append((name, surname, age))

    cls.sort()

    for name, surname, age in cls:
        print(f"{name}, {surname}, ({age})")

clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

mostrar_clientes(clientes)