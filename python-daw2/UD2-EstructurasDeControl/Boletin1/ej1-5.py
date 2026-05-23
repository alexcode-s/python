# Ejercicio 1
print("Ejercicio 1")
for i in range(0,10,1):
    print(i,end=" ")
print("End")
print()

# Ejercicio 2
print("Ejercicio 2")
for i in range(0,50,1):
    if i%2 == 0:
        print(i, end=" ")
print("End")

# Ejercicio 3
print("Ejercicio 3")
n = int(input("Ingresa un número: "))
for i in range(0,5,1):
    print(n*i, end=" ")

# Ejercicio 4
for i in range(0,10000,1):
    if i%7 == 0:
        if i%10 == 0:
            print(i)
        else:
            print(i, end=" ")
print()
# Ejercicio 5

number = int(input("Introduce un número: "))
if number.is_integer():
    if number%2 == 0:
        print("Es par")
    else:
        print("Es impar")
else:
    print("No es un número")



