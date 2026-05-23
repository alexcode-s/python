# Diccionarios

- **Concepto**
    - Es una colección:
        - No ordenada
        - Mutable
        - No permite claves duplicadas
    - Cada elemento está formado por un par clave-valor
    
    ```python
    diccionario = {'clave' : 'valor'}
    ```
    
- **Crear diccionarios**
    - Vacíos:
        
        ```python
        d1 = {}
        d2 = dict()
        ```
        
    - Con contenido inicial:
        
        ```python
        d3 = {'nombre': 'Sergio Freire', 'Edad':22, 'Activo': True}
        d4 = dict(color='Azul', modelo='Candy', submodelo='Outdoor', motor='2.0')
        ```
        
        - En d3 se usan claves literales entre comillas.
        - En d4, el constructor dict() permite asignar directamente pares clave=valor, pero si las claves son identificadores válidos (sin espacios ni mayúsculas).
- **Claves y valores**
    - Las claves pueden ser de distintos tipos (números, cadenas, tuplas inmutables, etc).
    - Los valores pueden ser de cualquier tipo (enteros, listas, diccionarios, etc).
    
    ```python
    d5 = {25: 'Charcutería Manolo', 26: 'Medias Puri', 28: 'Bar Paco'}
    ```
    
- **Acceder a valores**
    - Por clave (forma directa):
        
        ```python
        print(d5[26]) # Medias Puri
        ```
        
        - Si la clave no existe lanza KeyError
    - Con `.get()`
        
        ```python
        print(d3.get('Bar Paco')) # None
        print(d3.get('Bar Paco', 'Esa clave no existe')) # Mensaje personalizado
        ```
        
        - No lanza error si la clave no existe.
- **Recorrer diccionarios**
    - Por defecto, al recorrer un diccionario se itera sobre las claves:
        
        ```python
        for elemento in d5:
        	print(elemento) # Muestra las claves
        ```
        
    - Para mostrar clave y valor:
        
        ```python
        for clave in d5:
        	print(clave, d5[clave])
        ```
        
- **Métodos principales**
    - `keys()`: Devuelve una vista con todas las claves.
        
        ```python
        print(list(d5.keys())) # [25, 26, 28]
        ```
        
    - `values()`: Devuelve una vista con todos los valores.
        
        ```python
        print(list(d5.values()))
        # ['Charcutería Manolo', 'Medias Puri', 'Bar Paco']
        ```
        
    - `items()`: Devuelve una vista de tuplas (clave, valor).
        
        ```python
        print(list(d5.items()))
        # [(25, 'Charcutería Manolo'), (26, 'Medias Puri'), (28, 'Bar Paco')]
        ```
        
- **Añadir o modificar elementos**
    - Si la clave no existe, se añade, si ya existe, se sustituye su valor:
        
        ```python
        d5[30] = 'Bar Manolo' # Nueva clave
        d5[26] = 'Panadería Puri' # Reemplaza valor anterior
        ```
        
- **Eliminar elementos**
    - `pop(clave)`: Elimina una clave y devuelve su valor.
    - `popitem()`: Elimina el último elemento insertado.
    - `del d[clave]`: Elimina una clave concreta.
    - `clear()`: Vacía completamente el diccionario.
- **Longitud y pertenencia**
    - Número de elementos:
        
        ```python
        len(d5)
        ```
        
    - Comprobar si una clave existe:
        
        ```python
        if 25 in d5:
        	print('Existe la clave 25')
        ```
        
- **Diccionarios anidados**
    - Un valor puede ser otro diccionario:
        
        ```python
        d6 = {
        	'Activo': False,
        	'DNI': '28777666X',
        	'Teléfono': '655443322',
        	'Dirección': {'Calle': 'Mayor', 'Número': 7}
        }
        
        # Acceso
        print(d6['Dirección']['Calle'])
        ```
        
- **Copiar diccionarios**
    - Para evitar que dos variables apunten al mismo diccionario:
        
        ```python
        d7 = d5.copy() # Copia superficial
        ```
        
- **Unir diccionarios**
    - Se pueden combinar 2 diccionarios con el operador `|` :
        
        ```python
        nuevo = d3 | d4
        print(nuevo)
        ```
        
    - También se puede hacer así (no modifica nada):
        
        ```python
        dic1 = {"a": 1}
        dic2 = {"a": 99}
        
        dic3 = {**dic1, **dic2}
        ```
        
    - O con update() (hace modificaciones):
        
        ```python
        dic1 = {"a": 1, "b": 2}
        dic2 = {"c": 3, "d": 4}
        
        dic1.update(dic2)
        ```
        
- **Crear diccionarios anidados**
    
    ```python
    def agregarTarea(self, identificador, titulo, prioridad):
        if identificador in self.tareas:
            print(f"Error: ID {identificador} ya existente")
            return
    
        self.tareas[identificador] = {
            "titulo": titulo,
            "prioridad": prioridad,
            "realizada": False
        }
    
        print(f"Tarea '{titulo}' (ID: {identificador}) añadida.")
    ```
    
- **Comprobar existencia de clave**
    
    ```python
    dic = {"a": 1, "b": 2}
    
    if "a" in dic:
        print("La clave existe")
    
    ```