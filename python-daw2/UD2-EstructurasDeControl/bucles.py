for c in "Hola mundo":
    print(c, end="")
print("\nFin")

# Ejercicio: Recoger cadena por teclado e imprimirla sin ningún espacio
cadena = input("Introduce cadena: ")
for i in cadena:
    if i == " ":
        pass
    else:
        print(i,end=" ")
print()
# Otra solución al ejercicio
cadenaSinEspacios = ""
for i in cadena:
    if i!=" ":
        cadenaSinEspacios += i
print(cadenaSinEspacios)

'''

Bucle while

'''
i = 0
while i<10:
    print(i, end=" ")
    i+=1

