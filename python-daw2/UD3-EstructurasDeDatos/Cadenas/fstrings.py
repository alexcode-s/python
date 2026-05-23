nombre = 'Sergio'
edad = 22
sueldo = 1000.55
print("Mi nombre es %s, tengo %d años y cobro %.2f euros al mes" %(nombre, edad, sueldo))
'''
%s 
%d
%f
'''

# Con fstring
print(f"Mi nombre es {nombre}, tengo {edad} años y cobro {sueldo} euros al mes")

# Limitar decimales
print(f"Mi nombre es {nombre}, tengo {edad} años y cobro {sueldo:.2f} euros al mes")

# Porcentajes
ratio = 0.08394
print(f'Porcentaje: {ratio:.2%}')

# Separar en millares
habitantes = 7123456789
print(f'Población: {habitantes:,} habitantes')

# Espacio entre cifras
n1 = 45
n2 = 123
print(f'{n1:04d}\n{n2:04d}')

# Otra salida formateada
txt = 'Piton'
print(f'***{txt:<20}***')
print(f'***{txt:>20}***')
print(f'***{txt:^20}***')

# Mostrar variable con su valor
print(f'{n1=}\n{n2=}')

# fstring es un tipo de dato, se puede asignar a una variable
t = f'{n1=}\n{n2=}'
print(t)

# fstring de varias líneas
ficha = f"""
===========================
|| Ficha del profesor/a: ||
===========================
Nombre: {nombre}
Edad: {edad}
Salaro: {sueldo:.2f} euros
"""
print(ficha)

# Llamada a función
def devuelveNombre():
    return 'Sergio'

ficha2 = f"""
===========================
|| Ficha del profesor/a: ||
===========================
Nombre: {devuelveNombre()}
Edad: {edad}
Salaro: {sueldo:.2f} euros
"""
print(ficha2)

# Condicionales
numero = 32
print(f'¿Es par? {True if numero%2==0 else False}')