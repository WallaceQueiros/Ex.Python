dista = int(input('Informe a distância da sua viagem em Km: '))
dista_mini = dista * 0.50
dista_maxi = dista * 0.45
if dista <= 200:
    print('A disância de sua viagem é de {}Km e o valor a ser pago será de R${:.2f}'.format(dista, dista_mini))
else:
    print('A disância de sua viagem é de {}Km e o valor a ser pago será de R${:.2f}'.format(dista, dista_maxi))
