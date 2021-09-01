from time import sleep
preco_normal = float(input('Informe o valor do produto: '))
desconto1 = preco_normal - (preco_normal * 10) / 100
desconto2 = preco_normal - (preco_normal * 5) / 100
cartao = preco_normal + (preco_normal * 20) / 100


# MENU
print('''FORMAS DE PAGAMENTO.
[1] Dinheiro ou Cheque: 10% de DESCONTO. 
[2] À vista no cartão: 5% de DESCONTO.
[3] Em até 2x no cartão: preço NORMAL.
[4] 3x ou mais no cartão: 20% de JUROS.''')
opcao = int(input('Escolha a forma de pagamento: '))
print('Processando forma de pagamento..')
sleep(3)

# fim menu
# Condição seguidas
if opcao == 1:
    print(f'O produto vale R${preco_normal:.2f} com 10% de deconto ele sai por R${desconto1:.2f}.')
elif opcao == 2:
    print(f'O produto vale R${preco_normal:.2f} com 5% de desconto ele sai por R${desconto2:.2f}.')
elif opcao == 3:
    total_parcela = int(input('Quantas parcelas? '))
    parcela = preco_normal / total_parcela
    print(f'O produto vale R${preco_normal:.2f} em 2x no cartão o valor se mantem.')
    print(f'Sua compra vai ser parcelada em {total_parcela} e cada parcela vai custar {parcela:.2f}')
elif opcao == 4:
    total_parcela = int(input('Quantas parcelas? '))
    parcela = cartao / total_parcela
    print(f'Sua compra vai ser parcelada em {total_parcela}x, e terá 20% de JUROS.')
    print(f'O produto irá sair no valor de {cartao:.2f}, e cada parcela vai custar {parcela:.2f}, ')

else:
    print('A opção {} não é valida, digite as opções 1, 2, 3 ou 4 para efetuar a compra que deseja.')
# Fim condição
