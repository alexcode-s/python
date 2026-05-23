f = open("datos.bin", "rb")   # lectura
f = open("datos.bin", "wb")   # escritura
f = open("datos.bin", "ab")   # añadir al final
f = open("datos.bin", "rb+")  # lectura y escritura

# Leer el fichero entero
with open("datos.bin", "rb") as f:
    datos = f.read()

# Escritura
with open("salida.bin", "wb") as f:
    f.write(b'\x01\x02\x03\x04')

# Escribir objetos
datos = bytes([10, 20, 30, 40])
with open("salida.bin", "wb") as f:
    f.write(datos)

f.seek(0)      # inicio
f.seek(10)     # byte 10
f.seek(-5, 2)  # 5 bytes antes del final
pos = f.tell() # Saber dónde estás

# Ejemplo completo
import struct

datos = [
    (1, 2.5),
    (2, 3.5),
    (3, 4.5)
]

with open("datos.bin", "wb") as f:
    for entero, flotante in datos:
        f.write(struct.pack("i f", entero, flotante))

with open("datos.bin", "rb") as f:
    while True:
        bloque = f.read(struct.calcsize("i f"))
        if not bloque:
            break
        print(struct.unpack("i f", bloque))
