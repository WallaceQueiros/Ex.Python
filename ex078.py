valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Informe o valor para a posição {cont + 1}: ')))
print('=' * 39)
print(f'Você digitou os valores {valores}')
print(f'O maior número foi {max(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c + 1}... ', end='')
print(f'\nO menor número foi {min(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c + 1}... ', end='')
