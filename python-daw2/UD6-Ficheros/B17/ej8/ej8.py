import random

nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken", "Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin", "Kaneki", "Zoro", "Kirishima"]

n = int(input("Cuántos personajes tendrá tu partida: "))

if n > 1 or n <= 8:
    random.shuffle(nombres)
    random.shuffle(apellidos)
    try:
        with open("personajes.txt", "w") as file:

            while n > 0:
                file.write(f"{nombres[n-1]} {apellidos[n-1]}")
                print(f"{nombres[n-1]} {apellidos[n-1]}")
                n -= 1
    except:
        print("Error en el fichero")
else:
    print("Número no válido")