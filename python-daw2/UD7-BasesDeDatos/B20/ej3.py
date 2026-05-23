import mysql.connector

try:
    connection = mysql.connector.connect(user="root", password="1234",
                                         host="localhost", database="pokemondb")

    cursor = connection.cursor()

    print("Crear nuevo pokemon")
    print("----------------------------------------")
    nombre = input("Introduce el nombre:")
    peso = round(float(input("Introduce el peso:")), 1)
    altura = round(float(input("Introduce la altura:")), 1)
    print("----------------------------------------")

    queryId = "SELECT numero_pokedex FROM pokemon ORDER BY numero_pokedex DESC LIMIT 1"
    cursor.execute(queryId)
    id = cursor.fetchone()[0]

    statement = f"INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES ({id+1}, '{nombre}', {peso}, {altura})"
    cursor.execute(statement)
    connection.commit()

    cursor.close()
    connection.close()
except mysql.connector.Error as e:
    print(e)