pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja continuar? [Sim/Não]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Foram cadastrados {len(pessoas)} pessoas.')
print(f'O maior peso é de {maior}Kg. O maior peso foi de ', end='')
for dados in pessoas:
    if dados[1] == maior:
        print(f'{dados[0]}', end=',')
print()
print(f'O menor peso é de {menor}Kg. O menor peso foi de ', end='')
for dados in pessoas:
    if dados[1] == menor:
        print(f'{dados[0]}', end=',')
print()
