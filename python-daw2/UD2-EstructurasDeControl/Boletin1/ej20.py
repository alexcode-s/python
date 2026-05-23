import math

# Ejercicio 20
nums = [0]*4
for i in range(len(nums)):
    nums[i] = int(input(f'Introduzca el número {i+1}: '))

for i in range(1, len(nums)):
    j = nums[i]
    k = i-1
    while k >=0 and nums[k] > j:
        nums[k+1] = nums[k]
        k -= 1
    nums[k+1] = j
print(nums)

# Ejercicio 21
num = int(input('Número:'))

if num < 1:
    print('No es primo')
elif num == 2 or num == 3:
    print('Es primo')
else:
    rc = math.floor(math.sqrt(num))
    i = 2
    primo = True
    while i<=rc:
        if num%i == 0:
            print(f'El número {num} no es primo')
            i = rc+1
            primo = False
        else:
            i += 1
    if primo:
        print(f'El número {num} es primo')