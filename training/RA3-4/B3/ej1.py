# Programa que pida una contraseña por teclado 2 veces y si no coinciden la vuelva a pedir hasta que lo haga.

eq = False

while not eq:
    passwd = input("Contraseña: ")
    confirm = input("Confirmar contraseña: ")
    eq = True if passwd == confirm else False

print("Las contraseñas coinciden")