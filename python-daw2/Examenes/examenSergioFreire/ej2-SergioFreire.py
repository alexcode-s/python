from abc import ABC

class Producto(ABC):
    def __init__(self, codigo, numPaginas, titulo, autor, prestado):
        self.__codigo = codigo
        self.__numPaginas = numPaginas
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = prestado

    def codigo(self):
        return self.__codigo

    def titulo(self):
        return self.__titulo

    def autor(self):
        return self.__autor

    def prestado(self):
        return self.__prestado

    def paginas(self):
        return self.__numPaginas

class Libro(Producto):
    def __init__(self, codigo, numPags, titulo, autor, prestado, formato, disponibles, prestados):
        super().__init__(codigo, numPags, titulo, autor, prestado)
        self.__formato = formato
        self.__disponibles = disponibles # Modificar luego
        self.__prestados = prestados # Modificar luego

    def disponibiles(self):
        return self.__disponibles

    def formato(self):
        return self.__formato

class Comic(Producto):
    def __init__(self, codigo, numPags, titulo, autor, prestado, color):
        super().__init__(codigo, numPags, titulo, autor, prestado)
        self.__color = color

    def color(self):
        return self.__color

class Biblioteca():
    def __init__(self, producto=None):
        self.__stock = {}
        self.agregarProducto(producto)

    def agregarProducto(self, producto):
        if producto:
            if producto not in self.__stock and isinstance(producto, Libro):
                self.__stock[producto.codigo()] = {
                    'Paginas': producto.paginas(),
                    'Titulo': producto.titulo(),
                    'Autor': producto.autor(),
                    'Prestado': producto.prestado(),
                    'Formato': producto.formato(),
                    'Disponibiles': producto.disponibiles()
                }
            if producto in self.__stock and isinstance(producto, Comic):
                print(f'No puedo añadir el comic {producto.titulo()} porque ya existe')


    def listarStock(self):
        for codigo, prod in self.__stock.items():
            if isinstance(prod, Libro):
                print(f'({codigo}) {prod.autor()} - {prod.titulo()} - {prod.formato()} - {prod.disponibiles()} ejemplares')

            if isinstance(prod, Comic):
                print(f'({codigo}) {prod.autor()} - {prod.titulo()} - {prod.color()}')

libro1 = Libro('CO112', 900, 'Cien años de soledad', 'Mario Vargas Llosa', False, 'Papel', 20, 5)
comic1 = Comic('CO112', 900, 'Cien años de soledad', 'Mario Vargas Llosa', False, 'BN')

b1 = Biblioteca()
b1.agregarProducto(libro1)
b1.agregarProducto(comic1)

b1.listarStock()