velo = int(input('Informe a velocidade do condutor em Km: '))
multa = (velo - 80) * 7.00
if velo > 80:
    print('Sua velocidade foi {}Km, multado por execesso de velocidade.'.format(velo))
    print('O valor da sua multa será de R${:.2f}'.format(multa))
else:
    print('Sua velocidade foi {}Km,  não foi multado.'.format(velo))
    print('Boa viagem.')
