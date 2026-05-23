conjunto1 = {5,6,7,8}
conjunto2 = {5,6,7,8}
diferencias = conjunto1.intersection(conjunto2)
print(diferencias)

if len(diferencias) != len(conjunto1):
    print('Hay repeticiones')
else:
    print('No hay repeticiones')