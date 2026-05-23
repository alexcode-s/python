#!/usr/bin/python3
import datetime
from datetime import date, time, datetime, timedelta

# Fecha actual
hoy = datetime.today()
print(hoy)

# Fecha y hora actual
ahora = datetime.now()
print(ahora)

# Fechas
birthday = date(1968, 8, 18)
citaMedica = datetime(2025, 12,15)
despertador = time(7,30,0)
print(birthday)
print(citaMedica)
print(despertador)

# Formateos
ahora = datetime.now()
formateado1 = ahora.strftime('%H:%M')
print(formateado1)

formateado2 = ahora.strftime('%H:%-M') # Con guión no completará con ceros al final
print(formateado2)

formateado3 = ahora.strftime('%d-%m-%Y - %H:%M') # Ampliado
print(formateado3)

formateado4 = ahora.strftime('%D-%M-%Y - %H:%M')
print(formateado4)

formateado5 = ahora.strftime('%D-%M-%Y - %I:%M') # Hora en formato 12 horas
print(formateado5)

formateado6 = ahora.strftime('(%w)(%U)%a %d-%b-%y (%j) %I:%M')
print(formateado6)

formateado7 = ahora.strftime('%c')
print(formateado7)

formateado8 = ahora.strftime('%x')
print(formateado8)

formateado9 = ahora.strftime('%X')
print(formateado9)

cadena = '01-02-2025 14:30'
fecha = datetime.strptime(cadena,"%d-%m-%Y %H:%M")
print(fecha)
print(fecha.hour)
print(fecha.year)

if ahora > citaMedica:
    print('La fecha de ahora es posterior a tu cita médica')
else:
    print('La fecha de ahora es anterior a tu cita médica')

print(ahora)
nuevaFecha = ahora + timedelta(days=10, hours=2, weeks=1)
print(nuevaFecha)