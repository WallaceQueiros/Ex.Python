from random import randint
from time import sleep
from operator import itemgetter

players = dict({'Jogador 1': randint(1, 6),
                'Jogador 2': randint(1, 6),
                'Jogador 3': randint(1, 6),
                'Jogador 4': randint(1, 6)})
ranking = list()
print('Valores Sorteados')
for k, v in players.items():
    sleep(1)
    print(f'{k} tirou: {v} ')
print('=' * 26)
print('Ranking dos Jogadores')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar {v[0]} com: {v[1]}')
    sleep(1)
