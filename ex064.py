soma = 0
cont = 0
nume = 0
while nume != 999:
    nume = int(input('Digite um número:'))
    if nume != 999:
        soma += nume
        cont += 1
print(f'A soma dos número digitados vai ser de: {soma}')
print(f'Foram digitados {cont} números.')
