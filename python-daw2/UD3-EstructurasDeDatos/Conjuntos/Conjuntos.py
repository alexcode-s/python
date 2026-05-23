# No tienen orden
# No permite referenciar sus elementos por orden
# No permiten elementos repetidos
# Métodos distintos de Listas y Tuplas

conjunto1 = {'Ana','Pedro','Luis','Eva'}
print(conjunto1)

# Convertir lista en conjunto
conjunto2 = set(['Ana','Pedro','Luis','Eva'])
print(conjunto2)

# Recorrer conjunto (sin orden)
for nombre in conjunto1:
    print(nombre)

'''''
# Intento de recorrer lista referenciando su posición (da error)
for i in range(0,len(conjunto1)):
    print(conjunto1[i])
    
# Intento de referenciar por posición (da error)
print(conjunto1[0])
'''''

# Comprobar si un elemento está en un conjunto
if 'Ana' in conjunto1:
    print('Ana está en el conjunto')

# Añadir elementos al conjunto
conjunto1.add('Sergio')

# Eliminar elementos del conjunto. Si no existe da error (excepción)
conjunto1.remove('Sergio')

# Eliminar elementos de un conjunto sin que de error en caso de no existir
conjunto1.discard('Coche')

# Elimina y recupera el primer elemento del conjunto
conjunto1.pop()

# Eliminar todo el contenido de un conjunto
conjunto1.clear()


# Operaciones con conjuntos
profesPrimero = {'Natalia','José María','Pedro','Yago'}
profesSegundo = {'José María','Agustín','Puche','Pedro'}

# Intersección: Devuelve la intersección (los comunes) de ambos conjuntos
print(profesPrimero & profesSegundo)
# Method
print(profesPrimero.intersection(profesSegundo))


# Unión: Devuelve la intersección sin duplicados
print(profesPrimero | profesSegundo)
# Method
print(profesPrimero.union(profesSegundo))


# Diferencia (no conmutativa): Devuelve la diferencia de un conjunto
print(profesPrimero - profesSegundo)
print(profesPrimero - profesSegundo)
# Method
print(profesPrimero.difference(profesSegundo))
print(profesSegundo.difference(profesPrimero))


# Otra forma de hacer una intersección
intersection = profesPrimero & profesSegundo
print(intersection)

