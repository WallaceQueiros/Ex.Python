from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
print('Caso não tenha carteira de trabalho digite 0')
dados['CTPS'] = int(input('Carteira de Trabalho: '))
