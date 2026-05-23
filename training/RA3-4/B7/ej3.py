# Pedir al usuario un número del 1 al 12 y mostrar el nombre del mes correspondiente. Mostrar error si el número no
# se corresponde con ningún mes.

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
          "Julio", "Agosto", "Septiembre", "Octubre",
          "Noviembre", "Diciembre"]

n = int(input("Mes: "))

if 1 <= n <= 12:
    print(months[n-1])
else:
    print("El número no corresponde con ningún mes.")