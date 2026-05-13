# Programa que pida números entre el 1 y el 100 por teclado hasta que se escriba la
# palabra FIN (mayúsculas). Si se introduce una entrada no válida (número > 100,
# < 1 o cadenas de caracteres que no sean FIN) no se tendrá en cuenta pero el
# programa seguirá su curso. Cuando el programa finaliza (palabra FIN), se
# mostrará por pantalla el número de entradas válidas que se han realizado, sin
# contar esta última que sirve para finalizar el programa.

inp = ""
attempts = 1
n = 0
while inp != "FIN":
    inp = input("Número: ")
    if inp != "FIN":
        try:
            n = int(inp)
            if 0 < n <= 100:
                attempts += 1
            else:
                print("Valor fuera de rango")
        except (ValueError, TypeError):
            print("Valor incorrecto")

print(f"Intentos: {attempts}")