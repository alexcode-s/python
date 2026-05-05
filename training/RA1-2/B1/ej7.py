# Escribir un programa que pida un número por teclado al usuario que simule ser el precio
# de un artículo y escriba el resultado de aplicarle el IVA del 21%

price = int(input("Precio del artículo: "))
iva = 0.21 * price
total = price + iva

print(f"Precio inicial: {price}")
print(f"IVA: {iva}")
print(f"Precio total: {total}")
