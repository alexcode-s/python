# Modificar el programa anterior para que además, muestre  al final cuál ha sido el número mayor y el menor introducido
inp = ""
attempts = 0
n = 0
sum = 0
nums = []

while inp != "FIN":
    inp = input("Número: ")
    if inp != "FIN":
        try:
            n = int(inp)
            if 0 < n <= 100:
                attempts += 1
                sum += n
                nums.append(n)
            else:
                print("Valor fuera de rango")
        except (ValueError, TypeError):
            print("Valor incorrecto")
nums.sort()

print(f"Intentos: {attempts}")
print(f"Media aritmética de entradas válidas: {sum/attempts}")
print(f"Número menor introducido: {nums[0]}")
print(f"Número mayor introducido: {nums[-1]}")