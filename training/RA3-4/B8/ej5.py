# Programa que realice el descrifrado del mensaje. Como es imposible saber qué letras eran mayúsculas y cuáles minúsculas
# en el mensaje original, el mensaje descifrado debería aparecer con todas las letras en mayúsculas.

msg = input("Mensaje cifrado: ")
result = [""] * len(msg)
left = 0
right = len(msg) - 1

for i, c in enumerate(msg):
    if i % 2 == 0:
        result[right] = c
        right -= 1
    else:
        result[left] = c
        left += 1

print("".join(result))