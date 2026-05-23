import re
# Programa que pida al usuario una contraseña y compruebe que cumple con las siguientes condiciones:
# a. Debe tener al menos 8 caracteres y no más de 20.
# b. Debe tener al menos una letra mayúscula y una minúscula.
# c. Debe tener al menos un número.
# d. Debe tener un símbolo de entre los siguientes: _ - ! ? *
# Si la contraseña no es válida, se pide de nuevo, y así sucesivamente hasta que sea correcta. Una vez que es correcta
# se pide al usuario que la introduzca de nuevo, si coincide se informa al usuario y se termina el proceso. Si no
# coincide se vuelve a empezar el proceso.

def checkPasswd(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[_!?*\-]).{8,20}$"
    if re.fullmatch(pattern, password):
        return True
    return False

passwd = input("Contraseña: ")

while not checkPasswd(passwd):
    passwd = input("Contaseña no válida, inténtelo de nuevo: ")

print("Contaseña válida")
