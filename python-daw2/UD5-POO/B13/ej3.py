class Agenda():
    def __init__(self):
        self._tareas = {}

    def agregarTarea(self, id, titulo, prioridad):
        if id not in self._tareas:
            self._tareas[id] = {
                'Titulo': titulo,
                'Prioridad': prioridad,
                'Completada': False
            }
            print(f"Tarea '{titulo}' (ID: {id}) añadida.")
        else:
            print(f'Error: ID {id} ya existente')

    def eliminarTarea(self, id):
        if id in self._tareas:
            titulo = self._tareas[id]['Titulo']
            del self._tareas[id]
            print(f'Tarea con ID {id} ({titulo}) eliminada.')
        else:
            print(f'Error: No se encontró una tarea con ID {id}.')

    def marcarComoCompletada(self, id):
        if id in self._tareas:
            self._tareas[id]['Completada'] = True
        else:
            print(f'Error: No se encontró una tarea con ID {id}')

    def mostrarTareasCompletadas(self):
        print('- LISTADO DE TAREAS:')
        hay = False

        for id, tarea in self._tareas.items():
            if tarea['Completada']:
                print(f"[{id}] {tarea['Titulo']} (Prioridad: {tarea['Prioridad']})")
                hay = True

        if not hay:
            print('No hay tareas completadas')

    def mostrarTareasNoCompletadas(self):
        print('- LISTADO DE TAREAS:')
        hay = False

        for id, tarea in self._tareas.items():
            if not tarea['Completada']:
                print(f"[{id}] {tarea['Titulo']} (Prioridad: {tarea['Prioridad']})")
                hay = True

        if not hay:
            print('No hay tareas completadas')