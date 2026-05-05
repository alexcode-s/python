# Escribir un programa donde se muestren todos los números divisibles por 7 menores a 10000

print("Divisibles por 7: ")

for i in range(10000):
    if i % 7 == 0:
        print(i)
