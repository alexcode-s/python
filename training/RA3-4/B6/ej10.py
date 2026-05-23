import re
# Una dirección IP privada de clase C. Cuatro bytes en formato decimal separados por un punto. Los dos primeros tienen
# que ser siempre 192.168.
# Ejemplo: 192.168.30.30

ip = input("Dirección IP: ")
pattern = r"^192\.168\.(\d{1,3})\.(\d{1,3})$"
match = re.fullmatch(pattern, ip)

if match:
    b3, b4 = int(match.group(1)), int(match.group(2))

    if 0 <= b3 <= 255 and str(b3) == match.group(1) and 0 <= b4 <= 255 and str(b4) == match.group(1):
        print("IP válida")
    else:
        print("IP no válida")
else:
    print("IP no válida")


