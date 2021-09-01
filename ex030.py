from time import sleep
nume = int(input('Digite um número inteiro: '))
par = nume % 2
print('Verificando...')
sleep(2)
if par == 0:
    print('O numero {} é par.'.format(nume))
else:
    print('O número {} é impar.'.format(nume))