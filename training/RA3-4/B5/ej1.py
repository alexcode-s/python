import random
# Programa que genere 6 números aleatorios entre el 1 y el 49 sin que ninguno de ellos esté repetido
# (simulando una lotería primitiva).

nums = random.sample(range(1, 50), 6)
print(*nums)

'''
nums = set()

while len(nums) < 6:
    nums.add(random.randint(1, 49))

print(nums)
'''

