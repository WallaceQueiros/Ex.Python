nume = (int(input('Digite o 1° número: ')),
        int(input('Digite o 2° número: ')),
        int(input('Digite o 3° número: ')),
        int(input('Digite o 4° número: ')))

print(f'Você digitou os seguintes valores: {nume}')
print(f'O número 9 apareceu {nume.count(9)} vezes. ')
if 3 in nume:
    print(f'O número 3 aparece na posição {nume.index(3) + 1}°.')
else:
    print('O número 3 não aparece em nenhuma posição.')
print(f'Os números pares digitados foram: ', end=' ')
for n in nume:
    if n % 2 == 0:
        print(n, end=' ')
