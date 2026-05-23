# Las funciones deben ir siempre al principio.
def miFuncion(mensaje):
    # Dentro de las funciones, las variables son locales. No se pueden usar fuera de ellas.
    valor = 5
    print(mensaje,valor)

miFuncion('Hola mundo')

# Funciones con valores de retorno (return)
def saludo(nombreSaludar):
    return 'Hola' + nombreSaludar

nombre1 = 'Sergio'
saludo(saludo(nombre1))

# Funciones con 2 valores de retorno (return)
def saludo2(nombreSaludar, despedida):
    return 'Hola'+' '+nombreSaludar+' '+despedida

nombre2 = 'Sergio'
print((saludo2(nombre2,'que te vaya bien')))

# Devolver múltiples valores (se debe tener el mismo número de variables llamado a la función)
def devuelveNumeros():
    return 1, 2, 3

n1, n2, n3 = devuelveNumeros() # Devuelve una tupla con todos los valores
print(n1,n2,n3,sep='-')

# Paso de parámetros por valor: Con variables no se transmiten valores
def funcion(valor):
    valor *= 5
    print(valor)

n = 2
funcion(n)
print(n)

# Paso de parámetros por valor: Con listas se transmiten valores
def funcion1(valor):
    valor *= 5
    print(valor)

n1 = [2]
funcion1(n1)
print(n1)

# Valores por defecto en parámetros
def saludo3(nombreSaludar, despedida='te veo pronto'):
    return 'Hola'+' '+nombreSaludar+' '+despedida

nombre3 = 'Sergio'
print((saludo3(nombre2,'que te vaya bien')))
print(saludo3('Antonio'))

# Recibir todos los argumentos pasados por parámetros
def muestraProfes(veces,*nombres):
    print(nombres) # Recibe los parámetros en una tupla
    # Iterar
    for _ in range(veces):
        for n in nombres:
            print(n)
        print('-----')

muestraProfes(2,'Agustín')
muestraProfes(3,'José María','Ana','Puche')

def repiteNombre(veces, nombre):
    for _ in range(veces):
        print(nombre, end=' *** ')
    print('---')

datos = [2,'Pepe']
datos2 = [4,'Luis']
repiteNombre(*datos)
repiteNombre(*datos2)
repiteNombre(*[3,'Eva'])
