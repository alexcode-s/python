# isinstance: Se puede comprobar si es int, float, str, list.
if isinstance(5, int):
    print('Es un entero')
else:
    print('No es un entero')

# En negativo.
texto = 'hola'
if not isinstance(texto, int):
    print('No es un entero')
else:
    print('Es un entero')

# "Comentario" para saber qué devuelve una función.
def prueba(arg1, arg2) -> str:
    return 'Hola'

