import mysql.connector

class Pokemon():
    def __init__(self, nombre, npokedex, peso, altura):
        self._nombre = nombre
        self._npokedex = npokedex
        self._peso = peso
        self._altura = altura

    def mostrar(self):
        print(f"{self._nombre} (#{self._npokedex})")
        print(f"Peso: {self._peso}")
        print(f"Altura: {self._altura}")

def mostrarPokemons(n1, n2):
    try:
        connection = mysql.connector.connect(user='daw2', password='LaElipa',
                                           host='localhost', database='dwes1')

        pointer = connection.cursor()
        query = f"SELECT * FROM pokemon WHERE numero_pokedex BETWEEN {n1} AND {n2};"
        pointer.execute(query)

        lista = pointer.fetchall()
        if lista:
            for pokemon in lista:
                poke = Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[3])
                poke.mostrar()

        pointer.close()
        connection.close()
    except mysql.connector.Error as e:
        print(e)

mostrarPokemons(20, 40)