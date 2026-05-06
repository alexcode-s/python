import random

n = random.randint(1, 1000)
count = 1

while n != 666:
    print(n)
    n = random.randint(1, 1000)
    count += 1

print(n)