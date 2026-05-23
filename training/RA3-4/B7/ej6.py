import random
# Modificar el ejercicio anterior para que muestre en qué posición del array se encuentra el máximo y el mínimo.
# Si están repetidos y aparecen en más de una posición, debería de indicarlas todas.

n = int(input("Número: "))
nums = [random.randint(10, 1000) for _ in range(n)]

mx = max(nums)
mn = min(nums)
media = sum(nums) / len(nums)

pos_max = [i for i, num in enumerate(nums) if num == mx]
pos_min = [i for i, num in enumerate(nums) if num == mn]

print(*nums)
print(f"Número máximo: {mx} -> Posiciones: {pos_max}")
print(f"Número mínimo: {mn} -> Posiciones: {pos_min}")
print(f"Media aritmética: {media:.2f}")