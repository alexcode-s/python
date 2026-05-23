# Sintaxis básica

- **Definir clase**
    - Sintaxis:
        
        ```python
        class Persona:
        	def __init__(self, nombre, edad): # Constructor
        		self.nombre = nombre # Atributo
        		self.edad = edad # Atributo
        		
        	def saludar(self): # Método
        	print(f'Hola, soy {self.nombre} y tengo {self.edad} años')
        ```
        
- **Instanciar objeto**
    - Sintaxis:
        
        ```python
        p1 = Persona('Sergio', 20)
        p2 = Persona('Ana', 30)
        
        p1.saludar() # Hola, soy Sergio y tengo 20 años
        p2.saludar() # Hola, soy Ana y tengo 30 años
        ```
        
- **Encapsulación**
    - Sintaxis para controlar el acceso a los datos de los objetos:
        
        ```python
        class Cuenta:
        	def __init__(self, saldo):
        		self.__saldo = saldo # Atributo "privado"
        		
        	def ver_saldo(self):
        		print(f'Saldo actual: {self.__saldo}')
        ```
        
        - Los atributos con `__` no se pueden acceder directamente desde fuera.
- **Funciones mágicas**
    - Funciones predefinidas dentro de las clases que empiezan con `__`, como `__init__`, `__str__`, `__len__`, etc.
    - Sirven para definir el comportamiento interno de los objetos, es decir, cómo se comportan frente a operaciones integradas de Python (sumas, comparaciones, conversión a texto, etc).
    - Funciones mágicas de creación, representación y ciclo de vida:
        - `__init__` → Constructor.  Se ejecuta automáticamente al crear el objeto.
        - `__del__` → Destructor. Se ejecuta al eliminar el objeto (no muy usado).
        - `__str__` → Representación legible. Define cómo se muestra al usar print() o str().
    - Funciones máginas aritméticas:
        - `__add__` → Sumar valor.
        - `__sub__` → Restar valor.
        - `__mul__` → Multiplicación escalar.
            
            ```python
            class Vector:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y
            
                # suma: +
                def __add__(self, other):
                    return Vector(self.x + other.x, self.y + other.y)
            
                # resta: -
                def __sub__(self, other):
                    return Vector(self.x - other.x, self.y - other.y)
            
                # multiplicación escalar: *
                def __mul__(self, escalar):
                    return Vector(self.x * escalar, self.y * escalar)
            
                # representación legible
                def __str__(self):
                    return f"({self.x}, {self.y})"
            
            # Uso
            v1 = Vector(2, 3)
            v2 = Vector(1, 4)
            
            print(v1 + v2)  # (3, 7)
            print(v1 - v2)  # (1, -1)
            print(v1 * 3)   # (6, 9)
            ```
            
        - `__truediv__` → División real.
        - `__floordiv__` → División entera.
        - `__mod__` → Módulo.
        - `__pow__` → Potencia
            
            ```python
            class Numero:
                def __init__(self, valor):
                    self.valor = valor
            
                def __truediv__(self, other):     # /
                    return Numero(self.valor / other.valor)
            
                def __floordiv__(self, other):    # //
                    return Numero(self.valor // other.valor)
            
                def __mod__(self, other):         # %
                    return Numero(self.valor % other.valor)
            
                def __str__(self):
                    return str(self.valor)
            
            a = Numero(10)
            b = Numero(3)
            
            print(a / b)   # 3.3333333333333335
            print(a // b)  # 3
            print(a % b)   # 1
            ```
            
    - Funciones mágicas lógicas:
        - `__eq__` → Igualdad.
        - `__ne__` → Desigualdad.
        - `__lt__` → Menor que
        - `__le__` → Menor o igual
        - `__gt__` → Mayor que
        - `__ge__` → Mayor o igual
            
            ```python
            class Persona:
                def __init__(self, nombre, edad):
                    self.nombre = nombre
                    self.edad = edad
            
                def __eq__(self, otra):
                    return self.edad == otra.edad
            
                def __lt__(self, otra):
                    return self.edad < otra.edad
            
                def __gt__(self, otra):
                    return self.edad > otra.edad
            
                def __str__(self):
                    return f"{self.nombre} ({self.edad} años)"
            
            # Uso
            p1 = Persona("Sergio", 25)
            p2 = Persona("Ana", 30)
            
            print(p1 == p2)  # False
            print(p1 < p2)   # True
            print(p1 > p2)   # False
            
            ```
            
- **Decoradores**
    - Es una función que devuelve otra función.
    - Sirven para modificar o ampliar el comportamiento de una función, método o clase sin cambiar su código original.
    - Sintaxis:
        - `@classmethod`: Convierte un método normal en método de clase, es decir, que recibe la clase (cls) en lugar de la instancia (self). Se usa para crear objetos de formas alternativas o afectar atributos de clase.
            
            ```python
            class Persona:
                especie = "Humano"
            
                def __init__(self, nombre):
                    self.nombre = nombre
            
                @classmethod
                def cambiar_especie(cls, nueva):
                    cls.especie = nueva
            
            # Uso
            Persona.cambiar_especie("Cyborg")
            print(Persona.especie)  # Cyborg
            ```
            
        - `@staticmethod`: Convierte un método en función estática, es decir, no usa ni self ni cls. Se utiliza para definir funciones relacionadas con la clase, pero que no dependen de ella.
            
            ```python
            class Matematica:
                @staticmethod
                def sumar(a, b):
                    return a + b
            
            # Uso
            print(Matematica.sumar(5, 7))  # 12
            ```
            
        - `@property`: Convierte un método en un atributo de solo lectura, o también permite definir getters y setters de forma más limpia. Se usa para encapsular atributos.
            
            ```python
            class Circulo:
                def __init__(self, radio):
                    self._radio = radio  # atributo “privado”
            
                @property
                def radio(self):
                    return self._radio
            
                @radio.setter
                def radio(self, valor):
                    if valor <= 0:
                        raise ValueError("El radio debe ser positivo")
                    self._radio = valor
            
            # Uso
            c = Circulo(5)
            print(c.radio)   # usa el getter → 5
            
            c.radio = 10     # usa el setter
            print(c.radio)   # 10
            
            c.radio = -3     # ValueError: El radio debe ser positivo
            ```
            
        - `@<propiedad>.setter` (siempre después de definir el getter): Define un setter.
            
            ```python
            class Persona:
                def __init__(self, nombre, edad):
                    self._nombre = nombre     # atributo “privado”
                    self._edad = edad         # atributo “privado”
            
                @property
                def edad(self):               # getter
                    return self._edad
            
                @edad.setter
                def edad(self, valor):        # setter
                    if valor < 0:
                        raise ValueError("La edad no puede ser negativa")
                    self._edad = valor
            
            # Uso
            p = Persona("Sergio", 25)
            
            print(p.edad)   # accede al getter → 25
            
            p.edad = 30     # llama al setter
            print(p.edad)   # 30
            
            p.edad = -5     # ValueError: La edad no puede ser negativa
            ```