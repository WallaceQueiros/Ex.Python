dado_pessoa = dict()
list_pessoa = list()
soma = media = 0
while True:
    dado_pessoa.clear()
    dado_pessoa['nome'] = str(input('Informe seu nome: '))
    while True:
        dado_pessoa['sexo'] = str(input('Informe seu sexo: ')).strip().upper()[0]
        if dado_pessoa['sexo'] in 'MF':
            break
        print('Digite M ou F')
    dado_pessoa['idade'] = int(input('Informe sua idade: '))
    soma += dado_pessoa['idade']
    list_pessoa.append(dado_pessoa.copy())
    while True:
        respo = str(input('Deseja cadastrar mais alguém: ')).strip().upper()[0]
        if respo in 'SN':
            break
        print('Responda Sim ou Não')
    if respo == 'N':
        break
print('-' * 30)
media = soma / len(list_pessoa)
print(f'A) A média de idade é de {media:2.1f} ')
print(f'B) Foram cadastradas um total de {len(list_pessoa)} pessoas')
print(f'C) As mulheres cadastradas foram: ', end='')
for m in list_pessoa:
    if m['sexo'] == 'F':
        print(f'{m["nome"]}', end=', ')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in list_pessoa:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end='')