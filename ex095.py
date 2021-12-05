dados_jogador = dict()
gol = list()
while True:
    dados_jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input('Informe o número de partidas: '))
    for g in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {g + 1}: ')))
    dados_jogador['gols'] = gol[:]
    dados_jogador['total'] = sum(gol)
    print('=' * 30)
    print(f'O jogador {dados_jogador["nome"]} jogou {partidas} partidas. ')
    for p, go in enumerate(dados_jogador['gols']):
        print(f' => Na partida {p + 1}, fez {go} gols.')
    print(f'E ele fez um total de {dados_jogador["total"]} gols.')
