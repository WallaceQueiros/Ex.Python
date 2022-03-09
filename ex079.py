valores = list()
while True:
    numero = (int(input('Digite um valor: ')))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso. ')
    else:
        print('Valor duplicado não será adicionado. ')
    quest = str(input('Quer continuar SIM|Quer parar NÃO: ')).upper()[0]
    if quest == 'N':
        break
print('-='*30)
valores.sort()
print(f'Sua lista de número é {valores}')