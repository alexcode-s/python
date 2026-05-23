def macsValidas(mac):
    mac = str(mac)
    if ':' in mac:
        bte = mac.split(':')
        for i in bte:
           if i[0] > 'FF' or i[0] > 'ff':
               return False
    return True

macIn = input('Introduzca una dirección MAC: ')

if macsValidas(macIn):
    print(f'{macIn} es válida')
else:
    print(f'{macIn} no es válida')

# F4:8E:38:AF:F4:1C