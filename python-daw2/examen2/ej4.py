def divisoresComunes(n1, n2):
    if n1 > 0 and n2 > 0:
        divisoresN1 = set()
        divisoresN2 = set()
        for i in range(n1):
            i += 1
            if n1 % i == 0:
                divisoresN1.add(i)
        for i in range(n2):
            i += 1
            if n2 % i == 0:
                divisoresN2.add(i)
        divisoresComunes = divisoresN1 & divisoresN2
        print(f'Los divisores comunes de {n1} y {n2} son: {"".join(str(divisoresComunes))}')
    else:
        print('No puedo calcular los divisores comunes de esos números')

divisoresComunes(1725, 2500)
