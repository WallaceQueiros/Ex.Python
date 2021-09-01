preco1 = float(input('Informe o preço do produto sem desconto: '))
desc = (preco1 * 5) / 100
preco2 = preco1 - desc
print('O produto custa {:.2f}R$ porém, com desconto de 5% ele vai para {:.2f}R$'.format(preco1, preco2))
