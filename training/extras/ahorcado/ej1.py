frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")

resultado = ""
for c in frase:
    if c == letra:
        resultado += c
    elif c == " ":
        resultado += " "
    else:
        resultado += "*"

print(f"Resultado: {resultado}")