# Programa que pida por teclado el precio de un artículo y escriba el resultado de
# aplicarle el IVA del 21%. El resultado debe estar redondeado a 2 decimales.

price = float(input("Precio: "))
iva = price * 0.21
total = price + iva

print(f"Precio base: {price}")
print(f"IVA: {iva}")
print(f"Precio + IVA: {total:.2f}")
