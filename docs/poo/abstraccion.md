# Abstracción

- **Concepto**
    - Una clase abstracta es una clase que no se puede instanciar directamente. Se usa como modelo o plantilla para otras clases que heredan de ella.
        - Sirve para definir métodos comunes que todas las subclases deben tener.
        - Obliga a las clases hijas a implementar ciertos métodos definidos como abstractos.
    - En Python, las clases abstractas se definen con el módulo abc (Abstract Base Classes).
    - Ejemplo:
        
        ```python
        from abc import ABC, abstractmethod
        
        class Figura(ABC):
        	@abstractmethod
        	def area(self):
        		pass
        ```
        
        - Esta clase no se puede instanciar.
- **@abstractmethod**
    - Este decorador se usa dentro de una clase abstracta para marcar métodos que deben implementarse obligatoriamente en las subclases:
        
        ```python
        class Figura(ABC):
        	@abstractmethod
        	def area(self):
        		pass
        		
        	@abstractmethod
        	def perimetro(self):
        		pass
        ```
        
        - Toda subclas de Figura debe implementar ambos métodos, o también será abstracta
        
        ```python
        class Cuadrado(Figura):
        	def __init__(self, lado):
        		self.lado = lado
        		
        	def area(self):
        		return self.lado ** 2
        		
        	def perimetro(self):
        		return 4 * self.lado
        		
        c = cuadrado(5)
        print(c.area())
        print(c.perimetro())
        ```
        
        - Si faltara alguno de los métodos, Python lanzaría un error.
- **iter()**
    - Es una función incorporada que devuelve un iterador de cualquier objeto iterable (listas, tuplas, cadenas, diccionarios, etc).
        
        ```python
        lista = [1, 2, 3]
        it = iter(lista)
        
        print(next(it)) # 1
        print(next(it)) # 2
        print(next(it)) # 3
        ```
        
- **__iter__()**
    - Método mágico que permite que tus propios objetos sean iterables (es decir, que puedan usarse en bucles for o con next()).
    - Para crear un iterable personalizado, se definen 2 métodos mágicos:
        - `__iter__(self)` → Debe devolver un iterador (normalmente self).
        - `__next__(self)` → Devuelve el siguiente elemento o lanza “StopIteration”
    - Ejemplo:
        
        ```python
        class Contador:
        	def __init__(self, inicio, fin):
        		self.actual = inicio
        		self.fin = fin
        		
        	def __init__(self):
        		return self
        		
        	def __next__(self):
        		if self.actual <= self.fin:
        			valor = self.actual
        			self.actual += 1
        			return valor
        		else:
        			raise StopIteration
        			
        # Uso
        for numero in Contador(1, 5)
        	print(numero)
        	
        	# 1
        	# 2
        	# 3
        	# 4
        	# 5
        ```