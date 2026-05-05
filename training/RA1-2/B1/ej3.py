n = int(input("Número: "))
print(f"Múltiplos de {n}: ")

for i in range(1, 6):
    m = n * i
    print(f"{n} x {i} = {m}")
