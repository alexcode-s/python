# Modificar el programa anterior para que cuando coincidan ambas contraseñas se informe del número de intentos
# inválidos

eq = False
attempts = 0

while not eq:
    passwd = input("Contraseña: ")
    confirm = input("Confirmar contraseña: ")
    eq = True if passwd == confirm else False
    if passwd != confirm: attempts += 1

print("Las contraseñas coinciden")
print(f"Intentos fallidos: {attempts}")