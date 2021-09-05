nome = str(input('Informe seu nome: ')).strip()
CPF = float(input('Informe seu CPF: '))
print('O caixa possui nostas de R$50, R$20, R$10, R$1. ')
valor = int(input('Informe o valor que deseja sacar: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced}')
        print(f'Valor sacado de R${valor:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break