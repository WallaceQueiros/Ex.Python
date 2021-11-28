lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-' * 31)
print(f'Essa lista possui {len(lista)} elementos.')
(lista.sort(reverse=True))
print(f'Os valores em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 faz parte da Lista')
else:
    print('O número 5 não faz parte da Lista')
