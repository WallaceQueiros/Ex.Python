from math import radians, sin, cos, tan

angu = float(input('Digite o ângulo: '))
seno = sin(radians(angu))
cose = cos(radians(angu))
tange = tan(radians(angu))
print('O ângulo de {:.0f}° tem o SENO de {:.2f}'.format(angu, seno))
print('E tem o COSSENO de {:.2f}\nE tem a TANGENTE de {:.2f}'.format(cose, tange))
