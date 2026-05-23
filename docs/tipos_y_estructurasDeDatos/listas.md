# Listas

- **Listas**
    - Permiten almacenar datos de cualquier tipo.
    - Son mutables y dinámicas.
    - Lista vacía:
        
        ```python
        # Primera forma
        mi_lista = []
        
        # Segunda forma
        mi_lista2 = list()
        ```
        
    - Lista con elementos:
        
        ```python
        mi_lista = [1, 2, 3, "texto", True]
        
        # Iterar
        for elemento in mi_lista:
        	print(elemento)
        
        # Iterar
        for i in range(len(mi_lista)):
        	print(i, '-', mi_lista[i])
        ```
        
    - Concatenar listas:
        
        ```python
        # Primera forma
        nuevaLista = mi_lista + mi_lista2
        
        # Segunda forma
        mi_lista += mi_lista2
        
        # Tercera forma
        mi_lista.extend(mi_lista2)
        
        # Extra
        mi_lista.extend(mi_lista2+mi_lista3)
        ```
        
    - Comprobar si un elemento está en una lista o no:
        
        ```python
        lista = [3,6,8,9,2]
        
        # Comprobar si está en la lista
        if 6 in lista:
        	print('Está en la lista')
        	
        # Comprobar si no está en la lista
        if 6 not in lista:
        	print('No está en la lista')
        ```
        
    - Elegir elementos aleatorios:
        - choice(): Devuelve elementos aleatorios. Puede devolver repeticiones.
            
            ```python
            alumnos = ['Álvaro','Sara','Eva','Juan']
            print(random.choice(alumnos)) # ['Álvaro','Sara','Álvaro',''Eva','Juan']
            ```
            
        - sample(n): Devuelve n elementos aleatorios sin repeticiones. Devuelve lista nueva
            
            ```python
            print(random.choice(alumnos) # ['Sara','Álvaro',''Juan','Eva']
            ```
            
        - shuflle(): Mezcla aleatoriamente los elementos de una lista en el lugar (es decir, modifica la original).
            
            ```python
            numeros = [1,2,3,4,5]
            random.shuffle(numeros)
            print(numeros) # [3,5,1,4,2]
            ```
            
- **Métodos**
    - Agregar elementos:
        - `append(x)`: Agregar x al final.
        - `extend(iterable)`: Agrega varios elementos.
        - `insert(pos, x)`: Inserta x en la posición pos.
    - Eliminar elementos:
        - `remove(x)`: Elimina la primera aparición de x.
            
            ```python
            # Sin duplicado
            lista = [1,2,3,4,5]
            lista.remove(3)
            print(lista) # [1,2,4,5]
            
            #Con duplicados
            lista = [1,2,3,4,3,5]
            lista.remove(3)
            print(lista) # [1,2,4,3,5]
            ```
            
        - `pop([i])`: Elimina y devuelve el elemento de i (por defecto el último)
            
            ```python
            lista = [1,2,3,4,5]
            elemento = lista.pop() 
            print(elemento) # 5
            print(lista) # [1,2,3,4]
            ```
            
        - `clear()`: Vacía la lista completa.
    - Buscar y contar:
        - `index(x)`: Devuelve la posición de x.
            
            ```python
            lista = [1,2,3,4,3,5]
            print(lista.index(2)) # 1
            ```
            
        - `count(x)`: Devuelve cuántas veces aparece x.
            
            ```python
            lista = [1,2,3,4,3,5]
            elemento = lista.count(3)
            print('Está',elemento,'veces') # Está 2 veces
            ```
            
    - Ordenar y revertir:
        - `sort(reverse=False, key=None)`: Ordena la lista.
            
            ```python
            # Ordenar números ascendentemente (por defecto)
            lista = [2,3,1,5,4]
            lista.sort()
            print(lista) # [1,2,3,4,5]
            
            # Ordenar números descendentemente
            lista.sort(reverse=True)
            print(lista) # [5,4,3,2,1]
            ```
            
        - `reverse()`: Invierte el orden de los elementos.
    - Copiar
        - `copy()`: Crea una copia superficial.
            
            ```python
            numeros = [1,2,3,4]
            copia = numeros.copy()
            
            copia.append(5)
            
            print(numeros) # [1,2,3,4]
            print(copia) # [1,2,3,4,5]
            ```
            
    - Otros:
        - `list()`: Convierte cadenas de texto a listas. Cada caracter es un elemento de la lista.
            
            ```python
            lista = list()
            texto = 'Hola mundo'
            lista = list(texto)
            print(lista) # ['H','o','l','a',' ','m','u','n','d','o']
            ```
            
        - `str()`: Convierte listas a cadena de texto.
            
            ```python
            lista = [1,2,3,4,5]
            texto = str(lista)
            print(texto) # [1,2,3,4,5] -> Formato de lista, pero es un string.
            ```