import pickle

objetos = []
fin_fichero = False  # Variable de control del bucle

with open("datos.bin", "rb") as f:
    while not fin_fichero:
        try:
            # Intentamos leer un objeto
            obj = pickle.load(f)

            # Si se lee correctamente, lo guardamos y mostramos
            objetos.append(obj)
            print("Objeto leído:", obj)

        except EOFError:
            # Cuando no hay más objetos, cambiamos la condición
            print("Fin del fichero alcanzado.")
            fin_fichero = True

# Resultado final
print("Objetos finales:", objetos)
