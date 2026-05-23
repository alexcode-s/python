import random
# Modificar el programa anterior para que sea más difícil el descifrado haciendo que, de forma aleatoria, algunas letras
# cambien de mayúsculas a minúsculas en el cifrado.

msg = input("Mensaje: ")
result = []
left = 0
right = len(msg) - 1

while left <= right:
    n = random.randint(0, 1)
    if n == 0:
        result.append(msg[right].upper())
    else:
        result.append(msg[right])

    if left != right: result.append(msg[left])

    left += 1
    right -= 1

print("".join(result))