valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {cont + 1}: ')))
print('-'*37)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}, na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)}, na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
