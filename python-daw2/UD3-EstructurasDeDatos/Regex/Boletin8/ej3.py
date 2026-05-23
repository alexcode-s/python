import re

# Números de exactamente 9 dígitos
# Empiezan por 6, 7 u 8
# El resto son 8 dígitos más
# Sin espacios, guiones ni otros caracteres
p3 = r'^[678]\d{8}$'

n = input('Número de teléfono: ')

if re.fullmatch(p3, n):
    print('Número válido')
else:
    print('Número no válido')

# Ejercicio 4: Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido
# de dos dígitos, luego un espacio y a continuación un número de teléfono.
# Ejemplo +34 912233444

p4 = r'^\+\d{2} ?\d{9}$'

# Ejercicio 5: Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco.
# Las palabras no pueden contener números y deben de empezar ambas por una letra
# mayúscula.
# Ejemplo: Hola Mundo

p5 = r'^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$'

# Ejercicio 6: Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
# mayúsculas, las x letras minúsculas y los 0 dígitos.
# Ejemplo: AB12-xyZ-75

p6 = r'^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]-\d{2}$'

# Ejercicio 7: Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por
# un espacio. A continuación un espacio y la fecha de caducidad en formato MM/YY. El
# mes tiene que ser válido (entre 01 y 12)
# Ejemplo: 1234 5678 9012 3456 03/25

p7 = r'^\d{4}(?: \d{4}){3} (0[1-9]|1[0-2])/\d{2}$'

# Ejercicio 8: Un IBAN bancario de España. Las dos letras iniciales siempre tienen que ser ES
# Ejemplo: ES61 1234 3456 42 0456323532

p8 = r'^ES\d{2} (?: \d{4}){2} \d{2} \d{10}$'

# Ejercicio 9: Un número de 4 cifras mínimo y 8 cifras máximo
# Ejemplo: 12345

p9 = r'^\d{4,8}$'

# Ejercicio 10: Una dirección IP pública de clase C. Cuatro bytes en formato decimal separados por un
# punto. Los dos primeros tienen que ser siempre 192.168.
# Ejemplo: 192.168.30.30

p10 = r'^192\.168\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'

# EXTRAS
# Reglas
# nombre y apellido:
# Solo letras minúsculas (a–z)
# Al menos 2 letras cada uno
# Separados por un punto
# Dominio fijo: @empresa.es
# No se permiten números
# No se permiten guiones ni caracteres especiales
# Nada antes ni después del correo
# nombre.apellido@empresa.es

ej1 = r'^[a-z]{2,}\.[a-z]{2,}@empresa\.es$'

'''
Validar una contraseña con las siguientes condiciones todas obligatorias:
Longitud mínima 8 y máxima 12 caracteres
Debe contener al menos:
    una letra mayúscula
    una letra minúscula
    un dígito
No se permiten espacios
No se permiten caracteres especiales (solo letras y números)
Nada antes ni después de la contraseña
Ejemplos:
    Abcdef12
    XyZ12345
    PassWord9
'''

ej2 = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,12}$'
