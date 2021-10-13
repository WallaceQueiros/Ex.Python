valores = list(), list()
for n in range(1, 8):
    nume = int(input(f'Digite o {n}º valor: '))
    if nume % 2 == 0:
        valores[0].append(nume)
    else:
        valores[1].append(nume)
print('-' * 30)
valores[0].sort()
valores[1].sort()
print(f'Números pares: {valores[0]}')
print(f'Números ímpares: {valores[1]}')
