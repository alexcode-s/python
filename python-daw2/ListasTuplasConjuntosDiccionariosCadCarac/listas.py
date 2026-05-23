lista = ['Ana','Verónica','Luis','Rafael']

# Iterar lista
for nombre in lista:
    print(nombre)

# Iterar lista por índice
for i in range(len(lista)):
    print(i,'-',lista[i])

for i, nombre in enumerate(lista):
    print(i, '-', lista[i])

# Copias en listas: Las listas nunca se copian,
# al asignar una lista a otra variable, sólo se crea una referencia a la otra lista original
#num1 = 4
#num2 = num1
#num2 *= 2
#print(num1)

num1 = [4]
num2 = num1
num2[0] *= 2
print(num1)

# Copiar una lista
num3 = num1.copy()
print(num3)