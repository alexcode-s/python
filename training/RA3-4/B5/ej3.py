# Programa que cuenta las palabras que tiene una frase introducida previamente por teclado. Las palabras
# pueden estar separadas por más de un espacio pero siempre debe haber al menos uno. No se tendrán en
# cuenta los signos de puntuación como separadores.

phrase = input("Frase: ")
words = phrase.split()

print(f"{len(words)} palabras")