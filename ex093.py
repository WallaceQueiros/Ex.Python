dados = dict()
gol = list()
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Informe o número de partidas: '))
for g in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {g + 1}: ')))
dados['gols'] = gol[:]
dados['total'] = sum(gol)
print('=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas. ')
for p, go in enumerate(dados['gols']):
    print(f' => Na partida {p + 1}, fez {go} gols.')
print(f'E ele fez um total de {dados["total"]} gols.')
