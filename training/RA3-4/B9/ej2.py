# Añadir una función que sirva para añadir nombres al diccionario. La llamada sería:
# nuevoCliente(clientes, "Felipe", "Lotas", 76)
# La función debe añadir el nuevo cliente al diccionario con el formato correcto. Si este cliente ya existe, debería
# mostrar en consola un mensaje advirtiéndolo y preguntando si se quiere sobreescribir la edad o no.
def nuevoCliente(c, name, surname, age):
    key = f"{surname}, {name}"
    if key in c:
        opt = input("El cliente ya existe. ¿Desea sobreescribir la edad? (s/n): ")
        match opt:
            case "s":
                c[key] = age
            case "n":
                print("Cliente no modificado")
            case _:
                print("Opción inválida")
    else:
        c[key] = age
        print("Cliente creado")


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
nuevoCliente(clientes, "Alice", "Anon", 20)
mostrar_clientes(clientes)
nuevoCliente(clientes, "Alice", "Anon", 23)
mostrar_clientes(clientes)
