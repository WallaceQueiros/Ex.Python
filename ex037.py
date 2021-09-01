nume = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print(f'{nume} convertido para BINÁRIO é igual a: {bin(nume)[2:]}')
elif opcao == 2:
    print(f'{nume} convertido para OCTAL é igual a: {oct(nume)[2:]}')
elif opcao == 3:
    print(f'{nume} convertido para HEXADECIMAL é igual a: {hex(nume)[2:]}')
else:
    print(f'Não existe a opção {opcao}, tente as opções validas 1, 2 ou 3.')
