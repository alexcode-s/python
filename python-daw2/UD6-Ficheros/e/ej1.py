import pickle
import mysql.connector

class Pokemon:
    def __init__(self, numero, nombre, peso, altura, tipos):
        self.numero = numero
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipos = tipos

    def mostrar(self):
        print(f"#{self.numero} - {self.nombre}")
        print(f"Peso: {self.peso}kg")
        print(f"Altura: {self.altura}m")
        print(f"Tipo: {', '.join(self.tipos)}")
        print()


pokemons = []
lineas_erroneas = []

try:
    with open("pokemon.txt", "r", encoding="utf-8") as fichero:
        for linea in fichero:
            linea = linea.strip()
            linea_valida = True

            if linea == "":
                linea_valida = False

            if linea_valida:
                partes = linea.split(", ")
                if len(partes) < 4:
                    linea_valida = False

            if linea_valida:
                try:
                    numero = int(partes[0].replace(".", ""))
                except ValueError:
                    linea_valida = False

            if linea_valida and len(partes) >= 5:
                try:
                    nombre = partes[1]
                    peso = float(partes[2])
                    altura = float(partes[3])
                    tipos = partes[4:]
                except ValueError:
                    linea_valida = False
            else:
                if linea_valida:
                    linea_valida = False

            if linea_valida:
                pokemon = Pokemon(numero, nombre, peso, altura, tipos)
                pokemons.append(pokemon)
            else:
                if linea != "":
                    lineas_erroneas.append(linea)

except FileNotFoundError:
    print("Error: no se pudo abrir el fichero de texto")

# Mostrar pokemons leídos
for p in pokemons:
    p.mostrar()

# Mostrar líneas erróneas
if len(lineas_erroneas) > 0:
    print(f"{len(lineas_erroneas)} líneas erróneas en el fichero:")
    for linea in lineas_erroneas:
        print(linea)


# EJERCICIO 2 - FICHERO BINARIO

try:
    with open("pokemon.dat", "wb") as fichero_binario:
        pickle.dump(pokemons, fichero_binario)
except IOError:
    print("Error al escribir el fichero binario")

pokemons_leidos = []

try:
    with open("pokemon.dat", "rb") as fichero_binario:
        pokemons_leidos = pickle.load(fichero_binario)
except IOError:
    print("Error al leer el fichero binario")

# Mostrar pokemons leídos del binario
for p in pokemons_leidos:
    p.mostrar()



try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="password",
        database="pokemondb"
    )

    cursor = conexion.cursor()

    for p in pokemons:
        insertar = True

        # Comprobar si el Pokémon ya existe
        consulta = "SELECT numero FROM pokemon WHERE numero = " + str(p.numero)
        cursor.execute(consulta)

        if cursor.fetchone() is not None:
            print("Advertencia: el Pokémon con código", p.numero, "ya existe en la base de datos")
            insertar = False

        if insertar:
            insert_pokemon = (
                "INSERT INTO pokemon (numero, nombre, peso, altura) VALUES ("
                + str(p.numero) + ", '"
                + p.nombre + "', "
                + str(p.peso) + ", "
                + str(p.altura) + ")"
            )
            cursor.execute(insert_pokemon)

            for tipo in p.tipos:
                # Insertar tipo si no existe
                insert_tipo = (
                    "INSERT IGNORE INTO tipo (nombre) VALUES ('"
                    + tipo + "')"
                )
                cursor.execute(insert_tipo)

                # Obtener id del tipo
                select_tipo = (
                    "SELECT id FROM tipo WHERE nombre = '"
                    + tipo + "'"
                )
                cursor.execute(select_tipo)

                resultado = cursor.fetchone()
                tipo_id = resultado[0]

                # Relación pokemon - tipo
                insert_relacion = (
                    "INSERT IGNORE INTO pokemon_tipo (pokemon_numero, tipo_id) VALUES ("
                    + str(p.numero) + ", "
                    + str(tipo_id) + ")"
                )
                cursor.execute(insert_relacion)

    conexion.commit()
    conexion.close()

except mysql.connector.Error:
    print("Error al acceder o trabajar con la base de datos")


