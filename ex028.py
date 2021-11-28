import random
from time import sleep

P1 = int(input('Digite um número de 0 a 5: '))
num = random.randint(0, 5)
print('PROCESSANDO...')
sleep(3)
print('O número escolhido foi {}, errou ou acertou?'.format(num))
if P1 == num:
    print('Parabés você ganhou.')
else:
    print('Que pena você perdeu.')
    print('Tente outra vez. ')
