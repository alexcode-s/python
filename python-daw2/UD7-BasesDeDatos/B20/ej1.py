import mysql.connector

try:
    connection = mysql.connector.connect(user="root", password="1234",
                                         host="localhost", database="pokemondb")

    pointer = connection.cursor()
    query = "SELECT nombre, altura FROM pokemon WHERE altura > 1.5"
    pointer.execute(query)

    lista = pointer.fetchall()
    print(lista)

    pointer.close()
    connection.close()
except mysql.connector.Error as e:
    print(e)