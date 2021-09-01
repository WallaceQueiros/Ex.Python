'''print('=' * 26)
print('{:^26}'.format('10 TERMOS DE UMA PA'))
print('=' * 26)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,  + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')'''

print("=" * 26)
print('{:^26}'.format(' 10 TERMOS DE UMA PA '))
print("=" * 26)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(primeiro, primeiro + (10 - 1) * razao + razao, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')