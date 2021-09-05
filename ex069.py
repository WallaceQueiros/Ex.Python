cont_idade = cont_Masc = cont_Femi = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_Masc += 1
    if sexo == 'F' and idade < 20:
        cont_Femi += 1
    opcao = str(input('Quer Continuar [SIM/NÃO]: ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer Continuar [SIM/NÃO]: ')).strip().upper()[0]
    if opcao == 'N':
        print(f'{cont_idade} pessoas tem 18 anos ou mais.')
        print(f'{cont_Masc} homens foram cadastrados. ')
        print(f'{cont_Femi} Mulheres tem menos de 20 anos. ')
    if opcao == 'N':
        break
