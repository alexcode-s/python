try:
    with open("datos.txt", "r") as file:
        lines = file.readlines()
        nums = []
        valids = 0
        novalids = 0
        average = 0

        for line in lines:
            try:
                line = float(line)
                nums.append(line)
                valids += 1
            except:
                novalids += 1

        for n in nums: average += n
        average = average / len(nums)

        nums.sort()
        print(f"Número de datos válidos: {valids}")
        print(f"Número de datos inválidos: {novalids}")
        print(f"Mínimo: {nums[0]}")
        print(f"Máximo: {nums[-1]}")
        print(f"Media aritmética: {average}")

except:
    print("Error")