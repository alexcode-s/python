# Programa que reciba por teclado un número y muestre sucesivamente el resultado de ir dividiéndolo
# por dos sucesivamente hasta llegar a un número igual o menor a 1. Caso de ser necesario, los
# resultados se mostrarán con 2 decimales

n = float(input("Número: "))
res = n / 2
print(f"{res:.2f}")

while res >= 1:
    res = res / 2
    print(f"{res:.2f}")