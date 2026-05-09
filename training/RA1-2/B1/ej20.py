# Programa que pida 3 números por teclado en cualquier orden y los muestre en pantalla
# ordenados de mayor a menor.

nums = []
nums.append(int(input("Número 1: ")))
nums.append(int(input("Número 2: ")))
nums.append(int(input("Número 3: ")))

nums.sort()
print(nums)

