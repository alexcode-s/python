class Manga():
    def __init__(self, mangaka, japanTitle, genre, lastPub, espTitle=None):
        self._mangaka = mangaka
        self._japanTitle = japanTitle
        self._espTitle = espTitle
        self._genre = genre
        self._lastPub = lastPub
        self._collection = []

    @property
    def getMangaka(self):
        return self._mangaka

    @property
    def getJapanTitle(self):
        return self._mangaka

    @property
    def getEspTitle(self):
        return self._espTitle

    @property
    def getGenre(self):
        return self._genre

    @property
    def getLastPub(self):
        return self._lastPub

    @property
    def getCollection(self):
        return self._collection

    def setCollection(self, *n):
        for i in n:
            if i in self._collection:
                print(f'El número {i} ya se encuentra en la colección -> No se añadirá')
            else:
                self._collection.append(i)
                print(f'Número {i} añadido')

    def toObtain(self):
        obtain = []
        for n in range(self._lastPub):
            if n not in self._collection:
                obtain.append(n)
        print(f'Por obtener: {obtain}')

    def __str__(self):
        return (f'Mangaka: {self._mangaka} | Título en japonés: {self._japanTitle} | Título en español: {self._espTitle}'
                f' | Género: {self._genre} | Último: {self._lastPub} | Obtenidos: {self._collection} ')

m1 = Manga('Sergio', 'Arigato', 'Comedia', 20, 'Las aventuras de Paco')
m1.setCollection(1, 2, 7)
m1.toObtain()
print(str(m1))
m1.setCollection(3,4,2,1)

m1.toObtain()
print(str(m1))