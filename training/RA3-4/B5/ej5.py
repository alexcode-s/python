import random
# Programa que genere 100 números aleatorios comprendidos entre el 1 y el 50 (incluidos) y, posteriormente, obtenga el
# mayor, el menor y el que más veces se repite (y diga cuántas veces lo hace).

nums = [random.randint(1, 50) for _ in range(100)]
nums.sort()
freq = {}

for n in nums: freq[n] = freq.get(n, 0) + 1

max_repetition = max(freq.values())
max_rep = [num for num, freq in freq.items() if freq == max_repetition]

print(nums)
print(f"Mayor: {nums[0]}")
print(f"Menor: {nums[-1]}")
print(f"Más repetido: {max_rep[0]} {max_repetition}")