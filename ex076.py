print('='*39)
print('{:^39}'.format('LISTAGEM DE PREÇOS'))
print('='*39)
listagem = ('Lápis',    1.75,
            'Borracha',  2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor',  4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 2.50,
            'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('='*39)
