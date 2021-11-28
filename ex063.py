print('=' * 26)
print('{:^26}'.format('Sequência de Fibonacci'))
print('=' * 26)
nume = int(input('Digite p número de termos que quer mostrar: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -> {termo2}', end=' -> ')
cont = 3
while cont <= nume:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    cont += 1
    print(f'{termo3} -> ', end='')
print('')
print('FIM')
print(f'Quantidade de termos que apareceram: {cont}')
