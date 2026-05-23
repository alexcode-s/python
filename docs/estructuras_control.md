# Estructuras de control

- **Condicional if**
    - Uso de if-else
        
        ```python
        if condición:
        	# Bloque a ejecutar si condición es True
        else:
        	# Bloque a ejecutar si condición es False 
        ```
        
        - Ejemplo:
            
            ```python
            edad = int(input("Edad: "))
            if edad < 18:
            	print("Mayor de edad")
            else:
            	print("Menor de edad")
            ```
            
    - Uso de elif
        
        ```python
        if condición1:
        	# Bloque a ejecutar si condición1 es True.
        elif condición2:
        	# Bloque a ejecutar si condición2 es True.
        elif condición3:
        	# Bloque a ejecutar si condición3 es True.
        else:
        	# Bloque a ejecutar si ninguna condición es True.
        ```
        
    - Tabulaciones obligatorias
        
        ```python
        edad = int(input("Edad: "))
        if edad < 18:
        print("Mayor de edad") # -> Sin tabulación, dará error.
        else:
        	print("Menor de edad")
        ```
        
- **Bucle while**
    
    ```python
    while condición:
    	# Código a ejecutar
    ```
    
- **Bucle for**
    - Sintaxis general
        
        ```python
        for variable in iterable: # iterable puede ser una lista, cadena, rango, etc.
            # Bloque de código
        ```
        
    - Uso de `range()`
        
        ```python
        range(stop) # Empieza en 0, incrementa de 1 en 1, hasta stop -1.
        range(start,stop) # Empieza en start, incrementa de 1 en 1, hasta stop -1.
        range(start,stop,step) # Empieza en start, incrementa de step, hasta stop -1.
        ```
        
        - start → Número inicial (por defecto 0).
        - stop → Límite superior no incluido.
        - step → Incremento (por defecto 1, puede ser negativo).
- **Match**
    - Sintaxis:
        
        ```python
        match variable:
            case valor1:
                # bloque si variable == valor1
            case valor2:
                # bloque si variable == valor2
            case _:
                # bloque por defecto (como "default" en switch)
        ```