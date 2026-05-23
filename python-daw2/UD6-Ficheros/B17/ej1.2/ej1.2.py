import filecmp
def compararFicheros(file1, file2):
    return filecmp.cmp(file1, file2, shallow=False)

file1 = "file1.txt"
file2 = "file2.txt"

try:
    with open(file1, "w") as filen1, open(file2, "w") as filen2:
        filen1.write("Este es el fichero 1")
        filen2.write("Este es el fichero 1")
    print(compararFicheros(file1, file2))

except:
    print("Error al manipular el fichero")



