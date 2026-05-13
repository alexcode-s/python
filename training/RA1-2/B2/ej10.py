# Modificar el programa anterior para que muestre al final la media aritmética de las entradas válidas

inp = ""
attempts = 0
n = 0
sum = 0

while inp != "FIN":
    inp = input("Número: ")
    if inp != "FIN":
        try:
            n = int(inp)
            if 0 < n <= 100:
                attempts += 1
                sum += n
            else:
                print("Valor fuera de rango")
        except (ValueError, TypeError):
            print("Valor incorrecto")

print(f"Intentos: {attempts}")
print(f"Media aritmética de entradas válidas: {sum/attempts}")