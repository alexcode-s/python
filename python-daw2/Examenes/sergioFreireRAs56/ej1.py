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

pokemons = []
pokemonsnovalidos = []

def transformar(filename):
    try:
        with open(filename,'r') as file:
            line = file.readline()

            while line != "":
                block = line.split("-")
                poke = Pokemon(block[0], block[1], block[2], block[3], block[4])

                if len(block) == 5:
                    pokemons.append(poke)
                else:
                    pokemonsnovalidos.append(poke)

                line = file.readline()
    except:
        print("Error con el fichero")

transformar("pokedex.txt")

if pokemons:
    for pokemon in pokemons:
        pokemon.mostrar()

if pokemonsnovalidos:
    print(f"{len(pokemonsnovalidos)} Líneas erróneas en el fichero: ")
    for pokemon in pokemonsnovalidos:
        pokemon.mostrar()
