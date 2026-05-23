import math
import random

n = random.randint(10000000,50000000)
primo = False

while not primo:
    rc = math.floor(math.sqrt(n))
    i = 2
    while i <= rc:
        if n % i == 0:
            i = rc+1
            primo = True
        else:
            i += 1
