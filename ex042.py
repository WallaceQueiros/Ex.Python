reta_1 = float(input('Informe o primeiro segmento de reta: '))
reta_2 = float(input('Informe o segundo segmento de reta: '))
reta_3 = float(input('Informe o terceiro segmento de reta: '))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Este segmento forma um triangulo', end='')
    if reta_1 == reta_2 == reta_3:
        print(' Equilátero. ')
    elif reta_1 == reta_2 != reta_3 or reta_1 == reta_3 != reta_2 or reta_2 == reta_3 != reta_1:
        print(' Isósceles. ')
    elif reta_1 != reta_2 != reta_3:
        print(' Escaleno. ')

else:
    print('Não pode forma um triângulo. ')