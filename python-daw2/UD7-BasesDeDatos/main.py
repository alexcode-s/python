import mysql.connector

try:
    # Abrir conexión
    conexion = mysql.connector.connect(user='daw2', password='LaElipa',
                                       host='localhost', database='dwes1')

    # Ejecutar querys
    cursor = conexion.cursor()

    # Ejecutar sentencias
    query1 = "SELECT * FROM pokemon"
    #cursor.execute(query1) # Guarda tupla

    # Iterar - Mét 1
    '''
    for fila in cursor:
    print(fila)
    '''

    # Iterar - Mét 2
    '''
    lista = cursor.fetchall()
    print(lista)
    
    # 
    '''

    # Iterar - Mét 3
    '''
    query2 = "SELECT nombre, numero_pokedex FROM pokemon"
    cursor.execute(query2)

    for(pokemon, id) in cursor:
        print(id, "-", pokemon)
    '''

    # UPDATE
    query3 = "UPDATE pokemon SET nombre='Pokemon Cachas' WHERE nombre = 'Mewtwo'"
    cursor.execute(query3)
    print(cursor.rowcount, "filas afectadas por el query")
    query2 = "SELECT * FROM pokemon"
    cursor.execute(query2)
    for fila in cursor:
        print(fila)
    conexion.commit()

    # Cerrar cursor
    cursor.close()

    # Cerrar conexión
    conexion.close()
except mysql.connector.Error as err:
    print(err)
