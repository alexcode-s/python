# Programa que reciba un texto y devuelva un diccionario o una estructura similar donde las palabras de texto sean
# las claves y el número de veces que aparece cada una de ellas es su valor. La frase introducida no tiene signos
# de puntuación, el único separador entre palabras son los espacios y no se debe tener en cuenta tildes ni
# mayúsculas. Es decir: "qué" se considera una palabra distinta de "que" y "Como" es distinta de "como".

def diccionario(txt):
    words = txt.split()
    cnt = dict()

    for word in words:
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1

    print(words)
    print(cnt)

# texto = input("Texto: ").lower()
texto = "hola mundo cruel hola"
diccionario(texto)

