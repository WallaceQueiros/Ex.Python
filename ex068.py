from random import randint
from time import sleep
soma = cont = 0
resp1 = 'PAR'.upper()[0]
resp2 = 'IMPAR'.upper()[0]
while True:
    nume = int(input('Digite um valor: '))
    Maquina = randint(0, 10)
    soma = nume + Maquina
    par = soma % 2
    print('''PAR ou ÍMPAR: [P/I]: ''', end='')
    jogador = str(input('')).upper()[0].strip()
    print('UMDOLASI...')
    sleep(1.7)
    print('JÁ!')
    sleep(0.4)
    if jogador == resp1:
        CPU = resp2
    if jogador == resp2:
        CPU = resp1
    print(f'Você jogou {nume} e a Máquina jogou {Maquina}, TOTAL {soma}')
    if par == 0 and jogador == resp1 or par != 0 and jogador == resp2:
        print('Você Venceu!')
        cont += 1
    else:
        print("Você perdeu para a Maquina. 'HA' 'HA' 'HA'")
        print(f'GAME OVER!\nVocê venceu {cont} vezes.')
    if par == 0 and jogador == resp2 or par != 0 and jogador == resp1:
        break
