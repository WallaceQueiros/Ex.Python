soma = cont_produto = cont = 0
menor = maior = 0
barato = ''
caro = ''
while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        cont_produto += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_produto
    if cont == 1 or preco > maior:
        maior = preco
        caro = nome_produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar comprando? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        print(f'Total: {soma}\nVocê tem {cont_produto} produtos com mais de R$1000,00')
        print(f'O produto mais barato é {barato} e custa R${menor:.2f}')
        print(f'O produto mais caro é {caro} e custa R${maior:.2f}')
    if opcao == 'N':
        break
