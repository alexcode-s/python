# Programa que pida las notas obtenidas en un trimestre y nos muestre la media ponderada sabiendo que:
# 1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total.
# 2. La segunda corresponde a los ejercicios prácticos: 15%
# 3. La tercera nota del examen: 80%
# El resultado debería de mostrarse de dos formas:
# 1. Redondeado con 2 decimales (nota real).
# 2. Sin redondear y sin decimales (nota del boletín).

nums = []
total = 0

for i in range(3): nums.append(float(input(f"Nota {i+1}: ")))

nums[0] = nums[0] * 0.05
nums[1] = nums[1] * 0.15
nums[2] = nums[2] * 0.8

for n in nums: total += n

print(f"Nota real: {total:.2f}")
print(f"Nota del boletín: {round(total)}")