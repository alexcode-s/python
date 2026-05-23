import mysql.connector

try:
    connection = mysql.connector.connect(user="root", password="1234",
                                         host="localhost", database="pokemondb")

    pointer = connection.cursor()
    statement = "UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200"
    statement2 = "SELECT nombre, peso FROM pokemon WHERE peso > 200"
    pointer.execute(statement)
    pointer.execute(statement2)

    lista = pointer.fetchall()
    print(lista)

    pointer.close()
    connection.close()
except mysql.connector.Error as e:
    print(e)