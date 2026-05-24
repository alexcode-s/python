frase = input("Introduce una frase: ")
letra_mantener = input("Letra a mantener: ")

panel = ""
for c in frase:
    if c == letra_mantener:
        panel += c
    elif c == " ":
        panel += " "
    else:
        panel += "*"

print(f"Resultado: {panel}")

nueva_letra = input("Introduce una letra: ")
apariciones = frase.count(nueva_letra)
print(f"La letra {nueva_letra} aparece en {apariciones} ocasiones")

panel_nuevo = ""
for i in range(len(frase)):
    if frase[i] == nueva_letra:
        panel_nuevo += nueva_letra
    else:
        panel_nuevo += panel[i]

print(f"Resultado: {panel_nuevo}")