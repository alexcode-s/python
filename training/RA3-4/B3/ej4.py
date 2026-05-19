# Programa que pida por teclado una cadena de texto y la escriba sin espacios en blanco (si los hubiera). Además, debe
# indicar el número de espacios que ha encontrado y suprimido.

cad = input("Cadena: ")
sp = cad.count(" ")

if sp >= 1:
    print(cad.strip())
    print(f"Espacios encontrados: {sp}")
else:
    print("Sin espacios")