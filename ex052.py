'''nume = int(input('Informe um número inteiro: '))
mult = 0
for c in range(2, nume):
    if nume % c == 0:
        print('Multiplo de ', c)
        mult += 1

if mult == 0:
    print("É primo")

num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes ')
if tot == 2:
    print('E por isso ele É PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO! ')'''

nume = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, nume + 1):
    if nume % c == 0:
        tot += 1
        print(c, end=' - ')
print(f'\nO número {nume} é divisivel por {tot} números')
if tot == 2:
    print('Ele é um número PRIMO!')
else:
    print('Ele não é um número PRIMO!')
