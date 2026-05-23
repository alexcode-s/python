# Declarar diccionarios
d1 = {}
d2 = dict()
print(d1)
print('---------------------------')
# Crear diccionario con contenido
d3 = {'nombre': 'Sergio Freire', 'Edad': 22, 'Activo': True}
d4 = dict(color='Azul', modelo='Candy', submodelo='Outdoor', motor='2.0')
print(d3)
print(d4)
print('---------------------------')

# Las claves pueden ser alfanuméricas, no siempre numéricas.
d5 = {25: 'Charcutería Manolo', 26:'Medias Puri', 28:'Bar Paco'}
print(d5)
print('---------------------------')

# Acceder a un elemento
# Por clave
print(d5[26])
# Por valor
#print(d5["Bar Paco"])
# Con método get
print(d3.get('Bar Paco'))
# Con método get y mensaje de error
print(d3.get('Bar Paco', 'Esa clave no existe'))

# Recorrer diccionario
for elemento in d5:
    print(elemento)

for elemento in d5:
    print(elemento, d5[elemento])

# Devuelve las claves
print(list(d5.keys()))
# Devuelve valores
print(list(d5.values()))
# Devuelve una tupla con las claves y valores
print(list(d5.items()))

# Añadir elemento nuevo. Si ya existe la clave, sustituye el anterior por el nuevo
d5[30] = 'Bar Manolo'
print(list(d5.items()))


d6 = {'activo': False, 'dni':'28777666X','Teléfono': 655443322}
