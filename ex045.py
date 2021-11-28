from random import randint
from time import sleep

player = str(input('Informe seu nome no Jogo: '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Faça sua jogada: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
sleep(0.5)
print('=-' * 11)
print('Máquina jogou: {}'.format(itens[computador]))
print('{} jogou: {}'.format(player, itens[jogador]))
print('=-' * 11)

if jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
    print('EMPATOU!')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print(f'{player} VENCEU!')
else:
    print('Máquina VENCEU!')
