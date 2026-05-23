try:
    with open("redes.txt", "r") as file:
        lines = file.readlines()

        claseA = []
        claseB = []
        claseC = []

        for line in lines:
            suffix = int(line.split("/")[1])

            if suffix == 8:
                claseA.append(line.strip())
            if suffix == 16:
                claseB.append(line.strip())
            if suffix == 24:
                claseC.append(line.strip())


        print("Redes Clase A:")
        for net in claseA: print(net)
        print()

        print("Redes Clase B:")
        for net in claseB: print(net)
        print()

        print("Redes Clase C:")
        for net in claseC: print(net)

except:
    print("Error con el fichero")