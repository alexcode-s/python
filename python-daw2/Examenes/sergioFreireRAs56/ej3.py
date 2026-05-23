import pickle

# Este ejercicio está bien
class Pokemon():
    def __init__(self, nombre, npokedex, peso, altura, tipos):
        self._nombre = nombre
        self._npokedex = npokedex
        self._peso = peso
        self._altura = altura
        self._tipos = tipos.split(",")

    def mostrar(self):
        print(f"{self._nombre} (#{self._npokedex})")
        print(f"Peso: {self._peso}")
        print(f"Altura: {self._altura}")
        for tipo in self._tipos:
            print(f"Tipos: {tipo}", end="")
        print("\n")

def escribir(ruta, pokemons):
    try:
        with open(ruta, "wb") as file:
            pickle.dump(pokemons, file)

    except:
        print("Error al escribir")

def leer(ruta):
    try:
        with open(ruta, "rb") as file:
            pokemons = pickle.load(file)
            for pokemon in pokemons:
                pokemon.mostrar()

    except:
        print("Error al leer")

p1 = Pokemon("Chirokita", "152", "6.4", "0.9", "Planta")
p2 = Pokemon("Totodile", "158", "9.5", "0.6", "Agua")
p3 = Pokemon("Pikachu", "100", "5", "0.2", "Rayo")

escribir("pok.bin", [p1, p2, p3])
leer("pok.bin")