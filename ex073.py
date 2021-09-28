time = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Corinthians', 'Internacional',
        'Fluminense', 'Athletico-PR', 'Cuiabá')
#print('Os 5 primeiros colocados são: ')
#print('='*27)
#for primeiro in range(0, 5):
    #print(f'{time[primeiro]}', end=', ')
#print('')
#print('='*27)
#print('Os 4 ultimos colocados são: ')
#print('='*27)
#for ultimo in range(6, 10):
    #print(f'{time[ultimo]}', end=', ')
#print('')
#print('='*27)
#print('Tabela em Ordem alfabética:')
#print(sorted(time))
#print('='*27)
#for cont in range(9, len(time)):
    #print(f'O Cuiabá está na {cont}° posição')

print('='*27)
print(f'Os 5 primeiros colocados são: {time[0:5]}')
print('='*27)
print(f'Os 4 ultimos colocados são: {time[6:10]}')
print('='*27)
print(f'Tabela em Ordem alfabética: {sorted(time)}')
print('='*27)

for cont in range(9, len(time)):
    print(f'O Cuiabá está na {cont}° posição')
print('='*27)

