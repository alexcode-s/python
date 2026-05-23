from abc import ABC, abstractmethod
from datetime import date, time, datetime, timedelta

class Note(ABC):
    def __init__(self, title, description):
        self._title = title
        self._description = description
        self._date = datetime.now().strftime('%d-%m-%Y %H:%M')

    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def urgente(self):
        pass


class NormalNote(Note):
    COLORS = {'Amarillo', 'Verde', 'Blanco', 'Cyan'}
    def __init__(self, title, description, color):
        super().__init__(title, description)
        self._color = color if color in self.COLORS else "Blanco"
        self._date = datetime.now().strftime('%d-%m-%Y')

    def show(self):
        print(f'''
------------------------
 TÍTULO: {self._title}
 COLOR: {self._color}
 FECHA: {self._date}
------------------------
 {self._description}
------------------------
''')

    def urgente(self):
        return False

class NotaUrgente(Note):
    def __init__(self, title, description):
        super().__init__(title, description)
        self._color = "Rojo"

    def show(self):
        print(f'''
        ------------------------
         TÍTULO: {self._title}
         COLOR: {self._color}
         FECHA: {self._date}
        ------------------------
         {self._description}
        ------------------------
        ''')
    def urgente(self):
        return True

class Manager():
    def __init__(self):
        self._notes = []

    def createNormalNote(self, title, description, color):
        self._notes.append(NormalNote(title, description, color))

    def createUrgentNote(self, title, description):
        self._notes.append(NotaUrgente(title, description))

    def deleteNote(self, index):
        if 0 <= index < len(self._notes):
            note = self._notes[index]

            if note.urgente():
                confirm = input('¿Eliminar NOTA URGENTE? (S/N): ').lower()
                if confirm != 's':
                    print('Cancelado')
                    return
            self._notes.pop(index)

    def listNotes(self):
        ordenadas = sorted(self._notes, key=lambda note: note.urgente(), reverse=True)
        for i, note in enumerate(ordenadas):
            print(f'[{i}]')
            note.show()

manager = Manager()
manager.createNormalNote('Monday', 'Travel', 'Amarillo')
manager.createNormalNote('Sunday', 'My pet', 'Cyan')
manager.createUrgentNote('Aviso', 'Reunión de mañana')
manager.listNotes()

manager.deleteNote(1)
manager.listNotes()