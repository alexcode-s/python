# Programa que lea una frase y diga si es un palíndromo o no. Hay que tener en cuenta las mayúsculas y espacios.

cad = input("Introduce un texto: ").strip().lower().replace(" ", "")

if cad == cad[::-1]:
    print("El texto introducido es un palíndromo")
else:
    print("El texto introducido no es un palíndromo")
