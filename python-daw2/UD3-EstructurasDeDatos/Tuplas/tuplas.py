# Parecidos a listas
# Son inmutables
# Se usan para almacenar variables que no van a cambiar (inmutables)
# Los métodos de las listas funcionan con tuplas, a excepción de los que modifican valores de la tupla

# Listas se declaran con corchetes
lista = [1,2,3]

# Tuplas se declaran con paréntesis
tupla = (1,2,3)

# Al igual que las listas, pueden almacenar cualquier dato
tupla2 = ('Ana', 'Pepa', 'Pedro')

# Valores heterogéneos
tupla3 = ('María', 28.5, False)

# Otra forma de declarar una tupla (sin paréntesis). En listas no se puede declarar de esta manera
tupla4 = 4,5,6

# Tupla vacía (nunca se podrá modificar)
tupla5 = ()

# Tupla de un único elemento (similar a variables constantes)
tuplaUnicoElemento = (3.14159,)

# Convertir lista en tupla
tupla6 = tuple(lista)

# Convertir tupla en lista
lista2 = list(tupla4)

# Convertir tupla a string
texto = str(tupla6)

# Tuplas anidadas (con listas incluidas)
tupla7 = (1,2,(1,3,4),5,(6),[9,0,7])
print(tupla7[5]) # Lista dentro de la tupla
print(tupla7[5][2]) # Tercera posición de la lista dentro de la tupla

