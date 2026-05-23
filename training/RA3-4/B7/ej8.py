import random
# Implementación del juego del buscaminas. Generar un array de 2 dimensiones de 5 filas por 5 columnas. El tablero tendrá
# 5 minas que se colocarán de forma aleatoria en 5 posiciones del array. Las minas se representarán con un 1 y las posiciones
# sin mina con un 0.

ROWS = 5
COLS = 5
MINES = 5

tab = [[0 for _ in range(COLS)] for _ in range(ROWS)]
pos = [(r, c) for r in range(ROWS) for c in range(COLS)]
mines_pos = random.sample(pos, MINES)

for r, c in mines_pos:
    tab[r][c] = 1

print("Tablero: ")
for row in tab:
    print(" ".join(str(cell) for cell in row))