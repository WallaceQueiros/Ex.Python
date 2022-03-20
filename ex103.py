def ficha(jogador='Desconhecido', gols=0):
    if num_gols > 1:
        print(f'O jogador {jogador}, fez {gols} GOLS')
    else:
        print(f'O jogador {jogador}, fez {gols} GOL')


# Porgrama principal
nome_jogador = str(input('Nome do Jogador: '))
num_gols = str(input('Número de gols feitos: '))
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=num_gols)
else:
    ficha(nome_jogador, num_gols)
