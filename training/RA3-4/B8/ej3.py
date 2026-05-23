# Programa de cifrado que haga lo siguiente: mezcle los caracteres alternando entre las del principio y las del final
# del mensaje empezando siempre por el final.

msg = input("Mensaje: ")
result = []
left = 0
right = len(msg) - 1

while left <= right:
    result.append(msg[right])

    if left != right: result.append(msg[left])

    left += 1
    right -= 1

print("".join(result))
