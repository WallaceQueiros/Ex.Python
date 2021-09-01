sal1 = float(input('Informe seu salário sem aumento: '))
aument = (sal1 * 15) / 100
sal2 = sal1 + aument
print('O salário inicial era de {:.2f}R$, com o aumento de 15% foi para {:.2f}R$'.format(sal1, sal2))
