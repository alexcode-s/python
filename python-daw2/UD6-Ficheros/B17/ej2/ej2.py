try:
    with open("estadisticas.txt", "r") as file:
        content = file.readlines()
        hombres = content.count("Hombre\n")
        mujeres = content.count("Mujer\n")
        print(f"Hombres: {hombres}.")
        print(f"Mujeres: {mujeres}.")
        medidas = []
        file.seek(0)
        for row in file:
            value = row.strip()
            try:
                n = float(value)
                medidas.append(n)
            except ValueError:
                pass

        media = round(sum(medidas) / len(medidas), 2)
        print(f"Estatura media: {media}")
except:
    print("Error al leer el fichero")