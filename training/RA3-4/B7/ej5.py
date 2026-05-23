import random
# Pedir al usuario un número y crear un array de enteros de tantas posiciones como indique ese número. Rellenarlo con
# números aleatorios entre el 10 y el 1000 y finalmente mostrar cuál es el máximo, el mínimo y la media aritmética con
# 2 decimales

n = int(input("Introduzca un numero: "))

nums = [random.randint(10, 1000) for _ in range(n)]
nums.sort()
media = sum(nums)/len(nums)

print(*nums)
print(f"Número máximo: {nums[-1]}")
print(f"Número mínimo: {nums[0]}")
print(f"Media aritmética: {media:.2f}")
