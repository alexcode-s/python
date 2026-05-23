import random

cadena = input('Introduce una cadena: ')
cadena2 = list(cadena)
cadena3 = random.sample(cadena2,len(cadena))
cadena4 = str(cadena3).replace(']','').replace('[','').replace(',','').replace("'",'')
print(cadena4)