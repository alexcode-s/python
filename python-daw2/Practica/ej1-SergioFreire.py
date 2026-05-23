import random

# Pedir número de dados
dados = []
numDados = int(input('Número de dados: '))
stats = [0,0,0,0,0,0]
iguales = False
intentos = 1
cont = 0
total = 0

for i in range(numDados):
    dados.append(random.randint(1,6))

for i in range(len(dados)):
    n1 = dados[i]
    stats[n1-1] += 1

ls1 = str(dados).replace(',','-').replace('[','').replace(']','').replace(' ','')
print(ls1)

while not iguales and cont < len(dados):
    c = dados.count(dados[cont])

    if c == numDados:
        iguales = True
    else:
        cont += 1

    if cont == len(dados) and not iguales:
        intentos += 1
        dados.clear()
        cont = 0

        for i in range(numDados):
            dados.append(random.randint(1, 6))

        for i in range(len(dados)):
            n2 = dados[i]
            stats[n2 - 1] += 1

        ls2 = str(dados).replace(',','-').replace('[','').replace(']','').replace(' ','')
        print(ls2)

print(f'He tenido que lanzar los dados {intentos} veces para que todos sean iguales')
for i in range(len(stats)):
    print(f'El número {i+1} ha aparecido {stats[i]} veces')
    total += stats[i]
print(f'Total de apariciones de todos los números: {total}')

for i in range(len(stats)):
    porcentaje = round((stats[i]/total)*100,2)
    print(f'El número {i+1} ha salido el {porcentaje} % de las veces')

