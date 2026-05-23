import random

from reportlab.lib.validators import isNumber

# Ejercicio 6
num = int(input("Número: "))
if isNumber(num): # Comprobar si es un número entero (En casa: is_integer())
    if num%3 == 0:
        print(num,"es divisible por 3")
    else:
        print(num, "no es divisile por 3 ")
else:
    print("No es un número")

# Ejercicio 7
precio = float(input("Precio: "))
total = 0
if isinstance(precio,(int, float)): # Comprobar si es alguno de los tipos indicados
    suma = (precio*21)/100
    total = precio + suma
    print('Precio:',f"{total:.2f}") # Mostrar precio redondeado usando f"{n:.nf}" -> Ambas n son los números en cuestión.
else:
    print("No es un número")

#Ejercicio 8
importe = float(input('Importe a pagar: '))
numeroMeses = int(input('Plazo en meses: '))

if isinstance(importe,(int, float)) and isNumber(numeroMeses):
    cuota = importe/numeroMeses
    print('Cuota mensual:',f"{cuota:.2f}")
else:
    print('No es un número')

# Ejercicio 9
print(random.randint(0,50))

# Ejercicio 10
n1 = random.randint(1,6)
n2 = random.randint(1,6)
print(n1)
print(n2)

