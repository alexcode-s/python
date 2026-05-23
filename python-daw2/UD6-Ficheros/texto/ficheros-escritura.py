try:
    # Abrir fichero
    fichero = open('quijote.txt', 'r+')

    # ------------------ WRITE ------------------
    #fichero.write('En un lugar de La Mancha\n')
    #fichero.write('de cuyo nombre\n')
    #fichero.write('no quiero acordarme...\n')

    # ------------------ WRITELINES ------------------
    lista = ['En un lugar de La Mancha\n', 'de cuyo nombre\n', 'no quiero acordarme...\n']
    nums = ['1','2','3','4','5','6','7','8','9']
    fichero.writelines(lista)
    fichero.writelines(nums)
    print(f'Posición del cursor: {fichero.tell()}') # Cursor

    '''
    Modificar posición del cursor:
    seek(0) -> Inicio
    seek(0,n) -> Fin
    seek(n) -> Posición N contando desde el principio
    '''
    fichero.close()
except:
    print('Error al manipular el fichero')
