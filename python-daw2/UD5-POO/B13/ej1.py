from abc import ABC, abstractmethod

# Clase abstracta
class Persona(ABC):
    def __init__(self, nombre, apellido, grupo=None):
        self._nombre = nombre
        self._apellido = apellido
        self._grupo = grupo

    @abstractmethod
    def listar(self):
        pass

class Profesor(Persona):
    _DPTO = {'Informática', 'Empresa', 'Inglés'}
    def __init__(self, nombre, apellido, departamento, grupo=None):
        super().__init__(nombre, apellido, grupo)
        self._departamento = departamento if departamento in self._DPTO else 'Sin departamento'

    def listar(self):
        return f'{self._nombre} {self._apellido} - {self._departamento}'

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo, grupo=None):
        super().__init__(nombre, apellido, grupo)
        self._edad = edad
        self._ciclo = ciclo
        self._mayor = edad >= 18

    def listar(self):
        return f'{self._nombre} {self._apellido} ({self._edad}) - {'Mayor de edad' if self._mayor else 'Menor de edad'}'

class Ciclo():
    def __init__(self, nombre, grado):
        self._nombre = nombre
        self._grado = grado
        self._modulos = []

    def agregarModulo(self, modulo):
        self._modulos.append(modulo)

    def listar(self):
        print(f'Nombre: {self._nombre}, Grado: {self._grado}')
        print(f'Módulos:')
        for modulo in self._modulos:
            print(modulo.listar())

class Grupo():
    def __init__(self, nombre, ciclo, curso, tutor):
        self._nombre = nombre
        self._ciclo = ciclo
        self._curso = curso
        self._tutor = tutor
        self._alumnos = []

    def agregarAlumno(self, alumno):
        self._alumnos.append(alumno)

    def eliminarAlumno(self, alumno):
        self._alumnos.remove(alumno)

    def listar(self):
        print(f"""
            Nombre: {self._nombre}
            Ciclo: {self._ciclo.listar()}
            Curso: {self._curso}
            Tutor: {self._tutor.listar()}
            Número de alumnos: {len(self._alumnos)}
        """)
        print('Alumnos:')
        for alumno in self._alumnos:
            print(alumno.listar())

class Modulo():
    def __init__(self, nombre, year, horas, optativo):
        self._nombre = nombre
        self._year = year
        self._horas = horas
        self._optativo = optativo

    def listar(self):
        return f'{self._nombre}, Año: {self._year}, Horas: {self._horas}, Optativo: {self._optativo}'

# Ciclo
ciclo1 = Ciclo('Desarrollo de Aplicaciones Web', 'Superior')

# Módulos
modulo1 = Modulo('Programación en Python', 1, 8, 'No' )
modulo2 = Modulo('Desarrollo Web en Entorno Servidor', 2, 8, 'No')

# Agregar módulos al ciclo
ciclo1.agregarModulo(modulo1)
ciclo1.agregarModulo(modulo2)


# Profesor
profesor1 = Profesor('Javier','Puche', 'Informática')

# Alumno
alumno1 = Alumno('Carlos', 'Basanta', 15, ciclo1)
alumno2 = Alumno('María', 'Reyes', 20, ciclo1)

# Grupo
grupo1 = Grupo('DAW1', ciclo1, 2, profesor1)

# Agregar alumnos al grupo
grupo1.agregarAlumno(alumno1)
grupo1.agregarAlumno(alumno2)
grupo1.listar() 