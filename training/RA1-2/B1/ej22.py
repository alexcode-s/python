import random

n = random.randint(10000000, 50000000)
rc = round(n ** 0.5)
primo = True
i = 1

while primo:
    if i % n != 0 and n % n != 0:
        n = random.randint(10000000, 50000000)
        rc = round(n ** 0.5)
        i += 1
    else:
        primo = False

print(n)