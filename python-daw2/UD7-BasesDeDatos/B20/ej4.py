import mysql.connector

try:
    connection = mysql.connector.connect(user="root", password="1234",
                                         host="localhost", database="pokemondb")

    pointer = connection.cursor()
    print("Eliminar pokemon")
    print("-----------------------")
    id = int(input("Introduce el código del pokemon: "))
    statement = f"DELETE FROM pokemon WHERE numero_pokedex = {id}"
    pointer.execute(statement)
    connection.commit()

    pointer.close()
    connection.close()
except mysql.connector.Error as e:
    print(e)