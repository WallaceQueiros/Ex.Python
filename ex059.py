from time import sleep

nume = int(input('Informe o primeiro númeor: '))
nume2 = int(input('Informe o segundo número: '))
opcao = 0
maior = nume
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior nume
    [4] Novos números
    [5] Sair do Programa''')
    opcao = int(input('Escolha sua opção: '))
    print('PROCESSANDO SUA OPÇÃO...')
    sleep(1.5)
    if opcao == 1:
        print(f' A soma dos números {nume} + {nume2} é: {nume + nume2}')
    elif opcao == 2:
        print(f'A multiplicação dos números {nume} x {nume2} é: {nume * nume2}')
    elif opcao == 3:
        if nume2 > nume:
            maior = nume2
        print(f'O maior número entre {nume} e {nume2} é: {maior}')
    elif opcao == 4:
        nume = int(input('Informe o primeiro númeor: '))
        nume2 = int(input('Informe o segundo número: '))
    else:
        print('A opção não é valida, tente as opções [1/2/3/4 ou 5 para sair], Obrigado volte sempre. ')
if opcao == 5:
    print('Até logo, volte sempre. ')
