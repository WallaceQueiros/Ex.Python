nome = str(input('Informe o nome do funcionário: '))
sal = float(input('Informe o seu salário: '))
sal_mini = (sal * 15) / 100
sal_max = (sal * 10) / 100
if sal >= 1250:
    print('Você receberá um aumento de {:.2f}R$ (10%) no seu salário.'.format(sal_max))
else:
    print('Você receberá um aumento de {:.2f}R$ (15%) no seu salário.'.format(sal_mini))
