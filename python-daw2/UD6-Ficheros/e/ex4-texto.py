# Abrimos el fichero "datos.txt" en modo escritura ("w")
# Si no existe, se crea. Si existe, se sobrescribe.
with open("datos.txt", "w", encoding="utf-8") as f:
    # Escribimos una línea con nombre y edad
    f.write("Ana 25\n")

    # Escribimos otra línea
    f.write("Luis 30\n")

    # Escribimos una tercera línea
    f.write("Marta 22\n")

# Creamos una lista vacía donde guardaremos las edades
edades = []

# Abrimos el fichero en modo lectura ("r")
with open("datos.txt", "r", encoding="utf-8") as f:
    # Recorremos el fichero línea a línea
    for linea in f:
        # Separamos la línea en partes usando los espacios
        # Por ejemplo: "Ana 25\n" → ["Ana", "25"]
        nombre, edad = linea.split()

        # Convertimos la edad a entero y la añadimos a la lista
        edades.append(int(edad))

# Mostramos la lista final de edades
print(edades)

