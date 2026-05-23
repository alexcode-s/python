
try:
    with open("alumnos.txt", "r") as file:
        elements = file.readlines()
        for data in elements:
            name = data.split(":")[0].strip().split(",")[1]
            surname = data.split(":")[0].strip().split(",")[0]
            ratings = data.split(":")[1].strip().split(",")

            apt = True
            i = len(ratings)-1

            while apt and i >= 0:
                if float(ratings[i]) < 5:
                    apt = False
                i -= 1

            sum = 0
            for rate in ratings:
                sum += float(rate.strip())

            average = round(float(sum / len(ratings)), 1)

            if apt:
                print(f"{name} {surname} - {average}")


except:
    print("Error")