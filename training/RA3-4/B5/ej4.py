import re
# Programa que pida una cadena por teclado, luego cuente cuántas palabras hay en ella con cuatro o más vocales diferentes
# Por ejemplo, si se introduce la frase "Crisis constitucional por culpa del murciélago guineoecuatorial", debería de
# decir que 3. Se debe tener en cuenta que las vocales pueden ir en mayúsculas o no y son la misma letra. Se debe
# presuponer que ninguna vocal va acentuada de ninguna forma.

phrase = input("Cadena: ").lower()
count = 0

for word in phrase.split():
    vowels = {
        c
        for c in word
        if c in "aeiou"
    }
    if len(vowels) >= 4:
        count += 1
print(count)
