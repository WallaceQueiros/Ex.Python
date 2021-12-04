dado_pessoa = dict()
list_pessoa = list()
cont_pessoa = 0
while True:
    cont_pessoa += 1
    dado_pessoa['nome'] = str(input('Informe seu nome: '))
    dado_pessoa['sexo'] = str(input('Informe seu sexo: '))
    dado_pessoa['idade'] = str(input('Informe sua idade: '))
    respo = str(input('Deseja cadastrar mais alguém: ')).strip().upper()[0]
    if respo == 'N':
        break

print(dado_pessoa)
print(cont_pessoa)