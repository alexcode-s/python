# Programa que dada una matriz almacenada en un array, calcule su transpuesta y la almacene en otro diferente.
# El programa debería, además, dibujar en consola las matrices.

m = [
    [1, 2],
    [3, 4]
]

t = [list(fila) for fila in zip(*m)]

print("Matriz:")

for fila in m: print("|", *fila, "|")

print()
print("Transpuesta:")

for fila in t: print("|", *fila, "|")
