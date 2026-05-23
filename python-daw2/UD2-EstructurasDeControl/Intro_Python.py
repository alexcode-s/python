
# Comentario

# Salida por pantalla
print("Hola mundo")

# Comentario de bloque
'''
Comentario de bloque

'''
'''
Variables.
No es necesario declarar el tipo de variable
'''
edad = 56
print(edad)

# Las variables se pueden repetir (no recomendado, mala práctica)
edad = "Cincuenta y seis"
print (edad)

# Otras variables
precio = 54.6 # Decimales
acertado = True # Booleanos
print(acertado)

# Operadores aritméticos (Sólo nuevos, el resto son igual que otros lenguajes)
op1 = 5//2
op2 = 5%2
op3 = 5/2
print(op1, op2, op3)

# Cadenas de texto
texto = "Hola "
texto2 = texto+"mundo"
texto3 = "cruel"

print(texto2+texto3) # Concatenado

# Sobre print. Salida formateada. Se pueden incluir varios tipos de variables en print
n = 1
print(texto2,texto3, n)

# Uso de "end". Imprime el caracter o caracteres indicados (por defecto \n)
print(texto2,texto3, n, end=" ***")
print() # Salto de línea

# Uso de "sep". Sustituye el separador por defecto (espacio) por el que se le indique
print(texto2,texto3, n, sep="-")

# Recoger datos por teclado
edad1 = input("Introduce tu edad: ") # Similar a bash, se puede almacenar la entrada por teclado en una variable
print("Edad: "+edad1)

# Conversión de entrada a entero
edad2 = input("Introduce tu edad2: ")
if int(edad2) < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# Otra forma de conversión de entrada a entero
edad2 = int(input("Introduce tu edad2: "))
if edad2 < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# Conversión a float
edad2 = float(input("Introduce tu edad2: "))
if edad2 < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# Conversión a float de otra manera
edad2 = input("Introduce tu edad2: ")
if float(edad2) < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

'''
Condicionales

'''

# Condicional if

# Bucle for
for n in range(20,0,-1):
    print(n)
print("Fin del programa")