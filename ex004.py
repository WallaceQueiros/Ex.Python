algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algo))
print('{} Só tem espaços? '.format(algo), algo.isspace())
print('{} É um número? '.format(algo), algo.isnumeric())
print('{} É alfabético? '.format(algo), algo.isalpha())
print('{} É maiusculo? '.format(algo), algo.isupper())
print('{} É minusculo? '.format(algo), algo.islower())
print('{} É alfanumérico? '.format(algo), algo.isalnum())
print('{} É captalizada? '.format(algo), algo.istitle())
