import random
# Modificar el programa anterior para que sea el usuario quien introduzca dos números y se
# muestren los primos que hay entre ambos.

nums = []
nums.append(int(input("Número 1: ")))
nums.append(int(input("Número 2: ")))
nums.sort()

for i in range(nums[0], nums[1] + 1):
    if not any( i % n == 0 for n in range(2, int(i ** 0.5) + 1)):
        print(i)

