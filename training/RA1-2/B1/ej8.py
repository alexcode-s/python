# Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros (puede tener decimales)
# y el número de meses que contamos para pagarla (tiene que ser un número entero) y nos devuelva el dinero que
# tendríamos que pagar cada mes. No aplicamos intereses de ningún tipo y redondeamos a dos decimales.

quantity  = float(int(input("Ingrese la cantidad a pagar: ")))
months = int(input("Ingrese la cantidad de meses para pagar: "))
total = quantity / months

print(f"Cuota mensual: {total}")