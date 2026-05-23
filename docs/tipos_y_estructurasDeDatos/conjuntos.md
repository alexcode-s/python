# Conjuntos

- **Definición**
    - Es una colección desordenada, no indexada y sin elementos duplicados. Se usa cuando necesitas almacenar valores únicos y realizar operaciones matemáticas como uniones, interesecciones y diferencias. Características:
        - No permite duplicados: Cada elemento es único.
        - No tiene orden: Los elementos no tienen índice.
        - Son mutables: Se puede añadir o eliminar elementos.
        - Sus elementos deben ser inmutables: Se puede tener números, cadenas o tuplas, pero no listas ni otros sets.
- **Sintaxis**
    - Definición de un Set:
        
        ```python
        # Con llaves
        conjunto = {1,2,3,4}
        
        # Con el constructor set()
        conjunto = set([1,2,2,3])
        print(conjunto2) # {1,2,3}
        
        # Conjunto vacío
        vacio = set()
        ```
        
    - Operaciones básicas:
        
        ```python
        a = {1,2,3}
        b = {3,4,5}
        
        # Unión
        print(a | b) # {1,2,3,4,5}
        
        # Intersección
        print(a & b) # {3}
        
        # Diferencia 
        print(a - b) # {1,2}
        print(b - a) # {4,5}
        
        # Diferencia simétrica
        print(a ^ b) # {1,2,4,5}
        ```
        
- **Métodos**
    - `add(e)`: Añade un elemento.
        
        ```python
        numeros = {1,2,3}
        numeros.add(4)
        print(numeros) # {1,2,3,4}
        ```
        
    - `update(iterable)`: Añade varios elementos a la vez.
        
        ```python
        numeros = {1,2}
        numeros.update([3,4,5])
        print(numeros) # {1,2,3,4,5}
        ```
        
    - `remove(e)`: Elimina un elemento (error si no existe).
        
        ```python
        frutas = {"pera", "manzana", "uva"}
        frutas.remove("manzana")
        print(frutas) # {"pera", "uva"}
        # frutas.remove("kiwi") Lanza KeyError
        ```
        
    - `discard(e)`: Elimina un elemento (sin error si no existe).
        
        ```python
        frutas = {"pera", "manzana", "uva"}
        frutas.discard("kiwi")  # No pasa nada 
        print(frutas) # {"pera", "manzana", "uva"}
        ```
        
    - `pop()`: Elimina un elemento aleatoriamente y lo devuelve
        
        ```python
        numeros = {10, 20, 30}
        elemento = numeros.pop()
        print(elemento) # Ej: 10
        print(numeros) # {20, 30}
        ```
        
    - `clear()`: Vacía el conjunto.