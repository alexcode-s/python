# Programa que pida por teclado el radio de una circunferencia, admitiendo valores con decimales y calcule la longitud
# y el área de la circunferencia (redondeando a 5 decimales).
# area = 3.14159 * radio^2
# longitud = 2 * 3.14159 * radio

radio = float(input("Radio de circunferencia: "))

pi = 3.14159
pi2 = pi*pi
area = radio * pi2
longitud = 2 * pi * radio

print(f"Área: {area:.5f}")
print(f"Longitud: {longitud:.5f}")
