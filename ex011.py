altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('A altura da parede é de {}m e sua largura é de {}m e sua area será é de {}m²'.format(altura, largura, area))
print('Então será necessario {:.2f}L de tinta'.format(tinta))
