'''from math import  factorial
nume = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(nume)
print(f'O fatorial de {nume} é {f}.')'''

nume = int(input('Informe um número para calcular seu fatorial: '))
cont = nume
fat = 1
print(f'Calculando {nume}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')
