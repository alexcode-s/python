# Programa que pida 3 palabras por teclado en cualquier orden y las muestre por pantalla
# ordenadas alfabéticamente en orden ascendente.

words = []
words.append(input("Palabra 1: "))
words.append(input("Palabra 2: "))
words.append(input("Palabra 3: "))
words.sort()

print(words)