try:
    ciudadano = input("Introduce el nombre del ciudadano: ").lower()
    with open("delincuentes.txt", "r") as file:
        line = file.readline()

        while line != "":
            l = line.split(" ")

            if l[0] == "-":
                name = f"{l[1].lower()} {l[2][:-1].lower()}"
                edad = f"{l[3].strip()}"
                if ciudadano == name:
                    print(f"Edad: {edad} años")
                    line = file.readline()
                    background = []
                    while line != "" and not line.startswith("-"):
                        background.append(line.strip())
                        line = file.readline()

                    if background:
                        print("Antecedentes penales:")
                        for b in background:
                            print(b)
                    else:
                        print("Sin antecedentes penales")

            line = file.readline()
except:
    print("Error al leer el archivo")