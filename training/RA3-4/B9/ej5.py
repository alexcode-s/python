
fruits = {
    "aguacate": 4.35,
    "mandarina": 2.60,
    "kiwi": 3.75,
    "naranja": 1.80
}

fin = False
while not fin:
    buy = input("Fruta: ").lower().strip()
    if buy != "fin":
        if buy in fruits:
            try:
                kg = float(input("Kilogramos: "))
                price = fruits[buy]
                total = price * kg
                print(f"{kg} de {buy} cuestan {total:.2f} €")
            except ValueError:
                print("Cantidad no válida")
        else:
            print("No vendemos esa fruta")
    else:
        print("Hasta luego")
        fin = True
