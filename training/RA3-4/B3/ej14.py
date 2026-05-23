# Modificar el programa que validaba si un NIF era correcto comprobando si la letra que lo incorpora lo es.

nif = "12345678Z".lower()
letters = "trwagmyfpdxbnjzsqvhlcke"

n = int(nif[:-1])
letter = letters[n % 23]
print(n % 23)
print(letter)

print("NIF válido" if letter == nif[-1] else "NIF no válido")