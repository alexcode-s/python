# Programa que permita contar el número de veces que se repite una cifra en un número.

n = input("Número: ")
nums = list(n)
nums.sort()
freq = {}

for n in nums: freq[n] = freq.get(n, 0) + 1

for key in freq: print(f"{key} - Repeticiones: {freq[key]}")