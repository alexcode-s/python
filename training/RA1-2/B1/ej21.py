n = int(input("Número: "))
rc = round(n ** 0.5)+1
primo = True

for i in range(rc):
    if i % n != 0 and n % n != 0:
        primo = False

print("Primo" if primo else "No es primo")