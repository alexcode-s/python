'''
Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
ninguno de ellos esté repetido (simulando una lotería primitiva).
'''
import random

nums = [0]*6

for i in range(len(nums)):
    nums[i] = random.randint(1,49)

for i in range(len(nums)):
    apariciones = nums.count(nums[i])
    while apariciones > 1:
        nums.remove(nums[i])
        nums.append(random.randint(1,49))
        apariciones = nums.count(nums[i])
print(nums)