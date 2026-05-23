import re
# Validar IBAN bancario de España. Las dos letras iniciales siempre tienen que ser "ES".
# Por ejemplo: ES61 1234 3456 42 0456323532

iban = input("IBAN: ")
pattern = r"^ES\d{2} (\d{4} ){2}\d{2} \d{10}"

print("IBAN válido" if re.fullmatch(pattern, iban) else "IBAN no válido")
