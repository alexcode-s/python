# Sintaxis básica

- **Comentarios**
    - Comentario básico:
        
        ```python
        # Comentario en una sola línea
        ```
        
    - Comentario de bloque:
        
        ```python
        '''
        Comentario
        de
        bloque
        
        '''
        ```
        
- **Salida por pantalla**
    - Salida por pantalla simple:
        
        ```python
        print("Hola mundo")
        ```
        
    - Salida por pantalla de variables:
        
        ```python
        nombre = "Sergio"
        print(nombre)
        ```
        
    - Salida por pantalla de variables concatenadas
        - Usando `,`:
            
            ```python
            nombre = "Sergio"
            apellido = "Freire"
            print(nombre,apellido)
            ```
            
            - Salida por pantalla: “Sergio Freire”.
            - Usando este método, se agrega espacio en blanco por defecto entre variables.
        - Usando `+`:
            
            ```python
            nombre = "Sergio"
            apellido = "Freire"
            print(nombre+apellido)
            ```
            
            - Salida por pantalla: “SergioFreire”.
            - Usando este método, no se agrega espacio en blanco por defecto entre variables.
    - Modificar final de línea:
        
        ```python
        nombre = "Sergio"
        apellido = "Freire"
        print(nombre,apellido,end="***")
        ```
        
        - Salida por pantalla: “Sergio Freire***”.
        - Por defecto: end=”\n”.
    - Modificar método separador:
        
        ```python
        nombre = "Sergio"
        apellido = "Freire"
        print(nombre,apellido,sep="-")
        ```
        
        - Salida por pantalla: “Sergio-Freire”.
        - Por defecto: sep=” ” (Espacio en blanco).
- **Declaración de variables**
    - No es necesario declarar el tipo de variable.
    - El nombre de las variables puede repetirse, pero es mala práctica.
    - Declaración:
        
        ```python
        edad = 25 # Tipo entero -> No se declara el tipo de variable.
        precio = 54.6 # Tipo decimal.
        acertado = True # Booleano -> El primer caracter debe ir en mayúsculas.
        ```
        
- **Operadores aritméticos**
    
    ```python
    op1 = 5+5 # Suma.
    op2 = 5-5 # Resta.
    op3 = 5*5 # Multiplicación.
    op4 = 5/5 # División.
    op5 = 5%5 # Módulo de la división.
    op6 = 5//5 # Cociente de la división.
    ```
    
- **Operadores relacionales**
    - `==`: Igual
    - `!=`: Distinto
    - `>`: Mayor que
    - `<`: Menor que
    - `>=`: Mayor o igual que
    - `<=`: Menor o igual que
- **Cadenas de texto**
    - Ambas comillas son válidas.
    
    ```python
    nombre = "Sergio" # Con comillas dobles.
    apellido = "Freire"
    
    nombre = 'Sergio' # Con comillas simples.
    apellido = 'Freire'
    ```
    
    - Iterar cadenas:
        
        ```jsx
        texto = "Hola"
        
        for caracter in texto:
            print(caracter)
        ```
        
- **Recoger datos por teclado**
    - Se usa `input()`:
    
    ```python
    edad = input("Introduce tu edad: ")
    print("Edad: "+edad)
    ```
    
- **Conversión de tipos**
    - Convertir variables
        
        ```python
        edad = "50"
        edadInt = int(edad) # Convertido a entero
        edadFloat = float(edad) # Convertir a decimal
        ```
        
    - Convertir entrada por teclado
        
        ```python
        edad = int(input("Edad: "))
        print(edad)
        ```
        
        - Si se introduce algo que no sea el tipo indicado, dará error.
- **Redondeo de números**
    - `round(numero, n)`:
        - numero: Valor que se va a redondear.
        - n: Cúantos decimales se van a conservar (si no se especifica, redondea al entero más cercano).
    - `math.floor(n)`: Redondea hacia abajo.
    - `math.ceil(n)`: Redondea hacia arriba.
- **Números aleatorios**
    - `random.random()`: Devuelve un número float entre 0.0 y < 1.0
    - `random.randint(a, b)`: Devuelve un entero entre a y b (ambos incluidos).
        
        ```python
        x = random.randint(1, 100)
        print(x)
        ```
        
    - `random.uniform(a, b)`: Devuelve un número float entre a y b.
        
        ```python
        x = random.uniform(1.5, 5.5)
        print(x)
        ```
        
- **Comprobación de tipos**
    - `isdigit()`: Comprueba si el valor es un número no decimal. Si no es un número entero, dará error.
        
        ```python
        texto = 33
        print(texto.isdigit()) # True
        
        texto2 = 33.2
        print(texto.isdigit()) # False
        ```
        
    - `isaplha()`: Devuelve True si toda la variable es una cadena de caracteres:
        
        ```python
        texto = "Hola"
        print(texto.isaplha()) # True
        
        texto2 = 33
        print(texto.isalpha()) # False 
        ```
        
    - `isinstance(x, (int, float))`: Comprueba si x pertenece a int o a float