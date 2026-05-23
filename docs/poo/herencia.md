# Herencia

- **Concepto**
    - La clase padre o base define atributos y métodos comunes.
    - La clase hija o derivada hereda esos elementos y puede:
        - Usarlos directamente
        - Sobreescribirlos (reescribirlos)
        - Ampliarlos (añadir nuevos)
- **Sintaxis**
    
    ```python
    class ClasePadre
    	# Atributos y métodos comunes
    	pass
    	
    class ClaseHija(ClasePadre)
    	# Hereda todo de ClasePadre
    	pass
    ```
    
    - Ejemplo:
        
        ```python
        class Animal:
        	def hablar(self):
        		print('El animal hace un sonido')
        
        class Perro(Animal):
        	def hablar(self):
        		print('El perro ladra')
        		
        class Gato(Animal):
        	def hablar(self):
        		print('El gato maúlla')
        		
        p = Perro()
        g = Gato()
        
        p.hablar()
        g.hablar()
        ```
        
- **Uso de super()**
    - `super()` se usa en la clase hija para llamar al constructor o métodos de la clase padre.
        
        ```python
        class Persona:
        	def __init__(self, nombre):
        		self.nombre = nombre
        
        class Estudiante(Persona):
        	def __init__(self, nombre, carrera):
        		super().__init__(nombre)
        		self.carrera = carrera
        		
        e = Estudiante('Sergio', 'Informática')
        print(e.nombre, e.carrera) # Sergio Informática
        ```
        
    - `super()` evita reescribir código que ya existe en la clase base.
- **Herencia múltiple**
    - Una clase hereda de varias clases.
        
        ```python
        class A:
        	def metodoA(self):
        		print('Método de A')
        		
        class B:
        	def metodoB(self):
        		print('Método de B')
        
        class C(A, B):
        	pass
        	
        obj = C()
        obj.metodoA()
        obj.metodoB()
        ```
        
- **Sobreescritura de métodos**
    - La clase hija puede redefinir métodos del padre para cambiar su comportamiento:
        
        ```python
        class Vehiculo:
        	def arrancar(self):
        		print('El vehiculo arranca')
        		
        class Coche(Vehiculo):
        	def arrancar(self):
        		print('El coche arranca con motor de gasolina')
        ```
        
- **Polimorfismo y herencia**
    - El polimorfismo permite que distintas clases hijas redefinan el mismo método, y Python lo llame según el tipo real del  objeto:
        
        ```python
        for animal in [Perro(), Gato()]:
        	animal.hablar()
        ```
        
    - Cada objeto responde según su propia clase, aunque todos comparten el mismo me´todo `hablar()` heredado del padre.
- **Relaciones de herencia**
    - `isinstance()` y `issubclass()`: Sirve para verificar relaciones de herencia:
        
        ```python
        print(isinstance(p, Perro))     # True
        print(isinstance(p, Animal))    # True
        print(issubclass(Perro, Animal))# True
        ```
        
- **Encapsulación**
    - Los atributos “protegidos” (_*atributo) y “privados” (*__atributo) se heredan, pero deben manejarse con precacución:
        - `*_atributo*`: Accesible desde las subclases.
        - `__atributo`: Se “renombra” internamente (*ClasePadre*__atributo)