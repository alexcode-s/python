texto = "Hola mundo"
# De la posición 3 a la ocho (no incluida)
print('1',texto[3:8])

# Hasta la posición 8 (no incluida)
print('2',texto[3:8])

#
print('3',texto[-5:-2])

#

# Con variables
texto2 = texto[3:8]
print ('3',texto2)

#
texto3 = texto[::-1]
print('4',texto3)

print('5',texto[2:-2:2])
print('6',texto[::1])

# Métodos
print(texto.upper())
print(texto.lower())
print(texto.swapcase())
print(texto.find("m"))
print(texto.find("M"))

print(texto[2:4].upper())

print(texto.find("do"))
print(texto.count("do"))
print(texto.replace("do","X"))
print(texto.find("o",2,len(texto)-1))