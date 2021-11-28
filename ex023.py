nume = int(input('Digite um número entre 0 e 9999: '))
uni = nume // 1 % 10
deze = nume // 10 % 10
cente = nume // 100 % 10
milhar = nume // 1000 % 10
print('Número digitado foi: {}'.format(nume))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(deze))
print('Centena: {}'.format(cente))
print('Milhar: {}'.format(milhar))
