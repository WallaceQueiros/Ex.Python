from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('{:^30}'.format('MEGA SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        nume = randint(1, 60)
        if nume not in lista:
            lista.append(nume)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
