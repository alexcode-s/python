# Funciones

- **Definir una función**
    - Las funciones en Python se definen con la palabra clave def.
    - El código dentro de la función solo se ejecuta cuando se la llama.
    - Las variables declaradas dentro de una función son locales, es decir, existen  únicamente dentro de esa función y no pueden usarse fuera.
        
        ```python
        def miFuncion(mensaje):
        	valor = 5
        	print(mensaje, valor)
        
        # Llamada a función
        miFuncion('Hola mundo') # Hola mundo 5
        ```
        
- **Funciones con valor de retorno**
    - `return` devuelve un valor al punto donde se llama la función.
    - Después de ejecutar `return`, la función termina.
        
        ```python
        def saludo(nombreSaludar):
        	return 'Hola' + nombreSaludar
        	
        # Llamada
        nombre1 = 'Sergio'
        print(saludo(nombre1))
        ```
        
- **Funciones con múltiples parámetros**
    - Una función puede recibir más de un parámetro.
    - El orden en el que se pasan los argumentos debe coincidir conel orden definido.
        
        ```python
        def saludo2(nombreSaludar, despedida):
        	return 'Hola' + ' ' + nombreSaludar + ' ' + despedida
        	
        # Llamada
        print(saludo2('Sergio', 'que te vaya bien')) # Hola Sergio que te vaya bien 
        ```
        
- **Funciones que devuelven varios valores**
    - Se pueden devolver múltiples valores separados por comas.
    - Python los empaqueta automáticamente en una tupla.
    - Se pueden desempaquetar al recibirlos.
        
        ```python
        def devuelveNumeros():
        	return 1, 2, 3
        	
        # Llamada
        n1, n2, n3 = devuelveNumeros()
        ```
        
- **Paso de parámetros por valor**
    - En Python, los tipos inmutables (números, cadenas, tuplas) no pueden modificarase dentro de la función.
    - La variable `valor` dentro de la función es una copia, no el original.
    - Por eso, el `print(n)` final sigue mostrando 2.
        
        ```python
        def funcion(valor):
        	valor *= 5
        	print(valor)
        	
        n = 2
        funcion(n)
        print(n)
        ```
        
- **Paso de parámetros por referencia (listas y mutables)**
    - Las listas, diccionarios y objetos son mutables.
    - Al pasarlas como argumento, la función recibe una referencia al mismo objeto.
    - Por eso, si se modifica el contenido de la lista dentro de la función, se refleja fuera
    - Aunque en el ejemplo se usa `valor *= 5` (que crea una nueva lista internamente), si se hiciera `valor.append(3)`, sí se modificaría el objeto original.
        
        ```python
        def funcion1(valor):
        	valor *= 5
        	print(valor)
        
        n1 = [2]
        funcion1(n1)
        print(n1)
        ```
        
- **Valores por defecto en parámetros**
    - Los parámetros con un valor por defecto no son obligatorios al llamar a la función.
    - Si no se pasa ese argumento, se usa el valor asignado.
        
        ```python
        def saludo3(nombreSaludar, despedida='te veo pronto'):
        	return 'Hola' + ' ' + nombreSaludar + ' ' + despedida
        
        print(saludo3('Sergio', 'que te vaya bien')) # Hola Sergio que te vaya bien
        print(saludo3('Antonio')) # Hola Antonio te veo pronto
        ```
        
- **Argumentos variables**
    - *nombres agrupa todos los argumentos adicionales en una tupla.
    - Así se puede pasar un número variable de parámetros.
    - Muy útil cuando no se sabe cuántos valores recibirá la función.
        
        ```python
        def muestraProfes(veces, *nombres):
        	print(nombres)
        	for _ in range(veces):
        		for n in nombres:
        			print(n)
        		print('-----')
        		
        muestraProfes(2, 'Agustín')
        muestraProfes(3, 'José María', 'Ana', 'Puche')
        ```
        
- **Desempaquetado de argumentos con ***
    - El operador * desempaqueta una lista o tupla al pasarla como argumento.
    - Es decir, convierte `[2, ‘Pepe’]` en dos argumentos: `2` y `‘Pepe’`
        
        ```python
        def repiteNombre(veces, nombre):
        	for _ in range(veces):
        		print(nombre, end=' *** ')
        	print('---')
        
        datos = [2, 'Pepe']
        repiteNombre(*datos)
        ```