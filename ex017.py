'''CateOpost = float(input('Informe o cateto oposto: '))
CateAdja = float(input('Informe o cateto adjacente: '))
hipo = (CateOpost ** 2 + CateAdja ** 2) ** (1 / 2)
print('O Cateto Oposto é {} e o Ajacente é {} então, temos que a hipotenusa é {:.2f}'.format(CateOpost, CateAdja, hipo))'''

from math import hypot

CateOpost = float(input('Informe o cateto oposto: '))
CateAdja = float(input('Informe o cateto adjacente: '))
hipo = hypot(CateAdja, CateOpost)
print('A hipotenusa é {:.2f}'.format(hipo))
