# Excepciones

- **Definición**
    - Error detectado durante la ejecución del programa que interrumpe el flujo normal si no se maneja.
    - El sistema las usa para notificar y controlar errores de forma estructurada.
- **Sintaxis**
    - Básica
        
        ```python
        try:
        	# Código que puede fallar
        	x = 10 / 0
        except ZeroDivisionError:
        	# Qué hacer si ocurre ese error
        	print("No se puede dividir entre cero")
        ```
        
    - Con else:
        
        ```python
        try:
            n = int(input("Número: "))
        except ValueError:
            print("Debes ingresar un número")
        else:
            print("Todo fue bien")        # se ejecuta si NO hay error
        ```
        
- **Excepciones personalizadas**
    - Con raise:
        
        ```python
        def dividir(a, b):
            try:
                if b == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero")
                resultado = a / b
            except ZeroDivisionError:
                print("Error: división no permitida")
            else:
                print("Resultado:", resultado)
            finally:
                print("Operación finalizada\n")
        
        dividir(10, 2)
        dividir(10, 0)
        ```
        
    - Con assert:
        
        ```python
        def verificar_edad(edad):
            try:
                assert edad >= 18, "Debes ser mayor de edad"
            except AssertionError:
                print("Error: edad no válida")
            else:
                print("Acceso permitido")
            finally:
                print("Verificación completada\n")
        
        verificar_edad(20)
        verificar_edad(15)
        ```