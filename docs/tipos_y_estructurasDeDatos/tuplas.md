# Tuplas

- **Definición**
    - Colección ordenada e inmutable de elementos. Sirve para agrupar datos que no deben cambiar durante la ejecución del programa. Características
        - Ordenadas: Los elementos tienen un índice fijo.
        - Inmutables: No se pueden modificar, añadir ni eliminar.
        - Permiten duplicados.
        - Pueden contener distintos tipos de datos.
        - Se pueden recorrer con bucles o acceder por índice.
- **Sintaxis**
    
    ```python
    # Definición
    tupla = (1,2,3)
    
    # Definición sin paréntesis
    tupla2 = 1,2,3
    
    # Tupla de un solo elemento (coma obligatoria)
    tupla3 = (5,)
    ```
    
- **Acceso a los elementos**
    - Se hace igual que en las listas, usando índices:
        
        ```python
        t = ('a', 'b', 'c')
        print(t[0]) # a
        print(t[-1]) # c
        ```
        
- **Recorrer una tupla**
    
    ```python
    for elemento in t:
    	print(elemento)
    ```
    
- **Conversión entre lista y tupla**
    
    ```python
    lista = [1, 2, 3]
    tupla = tuple(lista)
    print(tupla) # (1, 2, 3)
    
    nueva_lista = list(tupla)
    print(nueva_lista) # [1, 2, 3]
    ```
    
- **Métodos**
    - `count(valor)`: Devuelve cuántas veces aparece un valor.
    - `index(valor)`: Devuelve el índice de la primera aparición del valor.
        
        ```python
        t = (1,2,2,3)
        print(t.count(2)) # 2
        print(t.index(3)) # 3
        ```