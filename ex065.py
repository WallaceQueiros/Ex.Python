soma = cont = media = maior = menor = 0
resp = 'S'.upper()[0]
resp2 = 'N'.upper()[0]
while resp == 'S':

    nume = int(input('Digite um número: '))
    soma += nume
    cont += 1
    if cont == 1:
        maior = menor = nume
    else:
        if nume > maior:
            maior = nume
        if nume < menor:
            menor = nume
    resp = str(input('Quer continuar:[S/N]: ')).upper()[0]
media = soma / cont

if resp == resp2:
    print(f'Você digitou {cont} números.')
    print(f'A média dos números que você informou é: {media:.2f}')
    if resp == resp2:
        print(f'O maior número foi {maior} e o menor foi {menor}.')
if resp == resp2:
    print('')
