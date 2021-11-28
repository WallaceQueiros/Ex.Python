from random import randint

nume = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números sorteados foram: {nume}')
print(f'O maior valor sorteado foi: {max(nume)}')
print(f'O menor valor sorteado foi: {min(nume)}')

"""nume = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('Os números sorteados foram: ', end='')
for n in nume:
    print(n, end=' ')
print(f'\nO maior número foi: {max(nume)}')
print(f'O menor número foi: {min(nume)}')"""
