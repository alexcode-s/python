# Función que sume un año a la edad del cliente. La llamada sería: cumpleCliente(clientes, "José", "Chuletón")

def cumpleCliente(c, name, surname):
    key = f"{surname}, {name}"

    if key in c:
        age = c[key]
        c[key] = age + 1


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
cumpleCliente(clientes, "Alice", "Anon")
mostrar_clientes(clientes)