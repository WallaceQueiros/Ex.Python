cidade = str(input('Digite o nome de uma cidade: ')).strip()
sepa = cidade.split()
print('O nome da cidade informada é {}'.format(cidade))
print('SANTO' in sepa[0].upper())