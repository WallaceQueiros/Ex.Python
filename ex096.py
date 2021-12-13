def area(largura, comprimento):
    area_area = largura * comprimento
    print(f'A área de um terreno com {area_largura}m (largura) x {area_comprimento}m (comprimento) é {area_area}m²')


print('Calculador De Area')
print('-' * 18)
area_largura = float(input('Largura(m): '))
area_comprimento = float(input('Comprimento(m): '))
area(area_largura, area_comprimento)
