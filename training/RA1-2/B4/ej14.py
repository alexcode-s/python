# Programa que lea una hora por teclado en formato 24 horas (HH:MM). El programa debería de decir si corresponde
# a la mañana (entre las 6 y las 11, ambas inclusive), si es una hora de la tarde (entre las 12 y 19, ambas inclusive)
#, si es de la noche (entre las 20 y las 23, ambas inclusive), si es de madrugada (entre las 0 y las 5, ambas inclusive)
# o bien si el formato no es correcto o no se corresponde con una hora real minutos de más de 60, horas negativas o por
# encima de 23, etc.

hours = input("Hora: ").split(":")
hour = int(hours[0])
mins = int(hours[1])

if mins > 0 and mins <= 60:
    if 6 <= hour <= 11:
        print("Mañana")
    elif 12 <= hour <= 19:
        print("Tarde")
    elif 20 <= hour <= 23:
        print("Noche")
    elif 0<= hour <= 5:
        print("Madrugada")
    else:
        print("Hora no válida")
else:
    print("Minutos no válidos")