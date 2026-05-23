nums = [0] * 2
capicuas = list()
ok = False

while not ok:
    ok = True
    nums[0] = int(input('Introduce el primer número: '))
    nums[1] = int(input('Introduce el segundo número: '))

    if nums[0] < 0 or nums[1] < 0:
        ok = False

    if nums[0] == nums[1]:
        ok = False

    if not ok:
        print('Error. Introduce el número de nuevo')

nums.sort()

for i in range(nums[0],nums[1]+1):
    if i < 10:
        capicuas.append(i)
    else:
        n1Ls = list(str(i))
        n2Ls = list(n1Ls)
        n2Ls.reverse()
        n1Str = str(n1Ls)
        n2Str = str(n2Ls)

        if n1Str == n2Str:
           capicuas.append(i)

capicuasStr = str(capicuas).replace('[','').replace(']','')

print(f'Números capicúas entre el {nums[0]} y {nums[1]}: {capicuasStr}')