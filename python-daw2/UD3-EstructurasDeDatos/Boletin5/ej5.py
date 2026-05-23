import random

nums = []

for i in range(100):
    rn = random.randint(1, 50)
    nums.append(rn)

nums.sort()
print(nums)
print(f'Número mayor: {nums[len(nums)-1]}')
print(f'Número menor: {nums[0]}')

freq = set()
for i in nums:
    freq.add(tuple([i,nums.count(i)]))

freqList = list(freq)
freqList.sort()



print(freqList)