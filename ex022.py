nome = str(input('Digite um Nome: ')).strip()
divi = nome.split()
print('O nome digitado foi {}'.format(nome))
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome completo possui {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui'.format(len(divi[0])))
