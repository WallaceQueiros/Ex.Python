perco = float(input('Informe quantos Km você percorreu com o carro: '))
dias = int(input('Informe a quantidade de dias do alugel do carro: '))
carro = (dias * 60.00)
rodado = (perco * 0.15)
total = (carro + rodado)

print('O carro andou {:.0f}Km e foi alugado para {} dias'.format(perco, dias))
print('O valor a ser pago pelo serviço é de R${:.2f}'.format(total))
