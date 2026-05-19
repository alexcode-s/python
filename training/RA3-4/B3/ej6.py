# Programa que pida por teclado una cadena de texto y la separe en dos distintas. En la primera de ellas estarían las
# letras que ocupan una posición par y en la segunda las que ocupan una posición impar. Por ejemplo si se escribe
# Hola Mundo la primera cadena sería "Hl ud" y la segunda "oaMno"

cad = input("Cadena: ")
pares = cad[::2]
imp = cad[1::2]

print(f"{pares} {imp}")