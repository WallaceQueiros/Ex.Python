from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
print('Caso não tenha carteira de trabalho digite 0')
dados['CTPS'] = int(input('Carteira de Trabalho: '))
if dados['CTPS'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['saldo'] = int(input('Salário: '))
    dados['aposenta'] = dados['contratacao'] - nasc + 35
    print('-'*30)
    print(f'Nome: {dados["nome"]}\nIdade: {dados["idade"]}\nCTPS: {dados["CTPS"]} '
          f'\nAno Contratação: {dados["contratacao"]}\nSalário: {dados["saldo"]}'
          f'\nAposentadoria: {dados["aposenta"]} anos ')
if dados['CTPS'] == 0:
    print('-' * 30)
    print(f'Nome: {dados["nome"]}\nIdade: {dados["idade"]}\nNão possui carteira de trabalho.')
