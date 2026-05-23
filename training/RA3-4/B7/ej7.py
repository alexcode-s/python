import random
# Pedir al usuario un número y crear un array de enteros de tantas posiciones como indique ese número. Se debe rellenar
# con números aleatorios entre el 10 y el 1000 y finalmente preguntar al usuario por la posición de la que quiere
# recuperar el valor. El programa mostrará el número de la posición indicada si esta existe y un error si se trata de
# recuperar una posición que no existe (menor a 0 o mayor a la longitud del array).

n = int(input("Número: "))
nums = [random.randint(10, 1000) for _ in range(n)]
print(*nums)
pos = int(input("Posición a recuperar: "))

try:
    rec = nums[pos-1]
    print(rec)
except IndexError:
    print("Error")