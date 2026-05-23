# Cadenas de caracteres

- **Slicing - Cadenas de texto**
    
    Permite extraer subcadenas de un string, o sublistas de una lista, indicando rangos de índices.
    
    Sintaxis:
    
    ```python
    secuencia[inicio:fin:salto]
    ```
    
    - inicio → Índice desde donde empieza (incluido) (por defecto 0).
    - fin → Índice hasta donde llega (no incluido) (por defecto len(secuencia)).
    - salto → Salto entre elementos (opcional).
    - Caso especial - Paso negativo:
        
        ```java
        secuencia[::-1]
        ```
        
        - inicio → Pasa a ser el final (len(secuencia))
        - fin → Pasa a ser el inicio ()
- **Métodos - Cadenas de texto**
    - Métodos de consulta:
        - `len(cadena)`: Longitud de la cadena.
        - `cadena.find(sub)`: Índice de la primera aparición (sino -1).
        - `cadena.index(sub)`: Como find, pero lanza error si no existe.
        - `cadena.count(sub)`: Cuántas veces aparece un substring.
        - `cadena.startswith(prefijo) / endswith(sufijo)`: Chequea prefijo/sufijo.
    - Métodos de transformación:
        - `cadena.replace(old,new)`: Sustituye old por new. old debe estar en la cadena. Siempre debe usarse reasignando.
        - `cadena.lower() / upper()`: A mayúsculas/minúsculas.
        - `cadena.capitalize()`: Primera letra en mayúscula.
        - `cadena.title()`: Cada palabra con mayúscula inicial.
        - `cadena.swapcase()`: Invierte mayúsculas o minúsculas.
        - `cadena.strip()`: Quita espacios al inicio y final.
            - `lstrip() / rstrip()`: Sólo izquierda o derecha.
        - `cadena.replace(old, new)`: Reemplaza texto.
    - Métodos de validación (devuelven booleanos):
        - `cadena.isalpha()`: Sólo letras.
        - `cadena.isdigit()`: Sólo dígitos.
        - `cadena.isalnum()`: Letras o números.
        - `cadena.isspace()`: Solo espacios.
        - `cadena.islower() / isupper()`: Todo en minúsculas/mayúsculas.
    - Métodos de división y unión:
        - `cadena.split(sep)`: Divide en lista.
        - `cadena.rsplit(sep, n)`: Divide desde la derecha.
        - `sep.join(lista)`: Une elementos con separador.
            
            ```python
            palabras = ["Hola", "mundo", "Python"]
            frase = " ".join(palabras)
            print(frase) # Hola mundo Python
            ```
            
        - `cadena.partition(sep)`: Divide en 3 partes (antes, sep, después).
- **Expresiones regulares**
    - Se usan para buscar, validar o manipular texto según un patrón.
    - Caracteres especiales comunes:
        - `\d`: Dígito de 0-9.
        - `\w`: Caracteres alfanuméricos (a-z, A-Z, 0-9 y _ ).
        - `\s`: Espacio en blanco (espacio, tabulación, salto de línea).
        - `.`: Cualquier carácter (menos salto de línea)
        - `^`: Inicio de línea
        - `$`: Fin de línea.
        - `*`: 0 o más repeticiones.
        - `+`: 1 o más repeticiones.
        - `?`: 0 o 1 repetición.
        - `{n}`: Exactamente n repeticiones.
        - `{n,m}`: Entre n y m repeticiones.
        - `[]`: Conjunto de caracteres.
        - `()`: Grupo de captura.
    - Funciones principales:
        - `re.search(patrón, texto)`: Busca la primera coincidencia en el texto.
            
            ```python
            texto = 'Mi número es 654-123-789'
            resultado = re.search(r"\d{3}-\d{3}-\d{3}", texto)
            # Tres dígitos, guion, tres dígitos, guion, tres dígitos
            print(resultado.group())
            ```
            
        - `re.match(patrón, texto)`: Comprueba si el texto empieza con el patrón.
        - `re.findall(patrón, texto)`: Devuelve todas las coincidencias en una lista.
        - `re.finditer(patrón, texto)`: Devuelve un iterador con objetos Match.
        - `re.sub(patrón, reemplazo, texto)`: Reemplaza las coincidencias por otro texto.
        - `re.split(patrón, texto)`: Divide el texto según el patrón.