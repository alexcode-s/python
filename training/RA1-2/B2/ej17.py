# Programa que reciba por teclado una temperatura en cualquiera de las tres unidades básicas (Celcius, Farenheit o Kelvin)
# y la devuelva en las otras dos. El programa reconocerá la unidad que se ha usado al introducir la entrada por teclado
# porque irá acompañado de una letra que lo indique. Por ejemplo 12C, 280.57K o 98.6F. Se admitirán decimales en la entrada
# y se devolverá el resultado con 2 decimales.
# Cº -> Fº: Fº = Cº * 1.8 + 32
# Fº -> Cº: Cº = (Fº-32) % 1.8
# Kº -> Cº: Cº = Kº - 273.15
# Cº -> Kº: Kº = Cº + 273.15
# Fº -> Kº: Kº = 5/9 (Fº-32) + 273.15
# Kº -> Fº: Fº = 1.8 (Kº-273.15) + 32
def printResults(temperature ,baseUnit, ud1, ud2, u1, u2 ):
    print(f"{temperature}{baseUnit} -> {ud1} = {u1:.2f}")
    print(f"{temperature}{baseUnit} -> {ud2} = {u2:.2f}")

temp = input("Temperatura: ")
unit = temp[-1:]
n = float(temp[:-1])

match unit:
    case "C":
        fh = n * 1.8 + 32
        kv = n + 273.15
        printResults(n, "C", "F", "K", fh, kv)
    case "F":
        cs = (n - 32) / 1.8
        kv = 5/9 * (n - 32) + 273.15
        printResults(n, "F", "C", "K", cs, kv)
    case "K":
        cs = n - 273.15
        fh = 1.8 * (n - 273.15) + 32
        printResults(n, "K", "C", "F", cs, fh)
    case _:
        print("Valor no válido.")

