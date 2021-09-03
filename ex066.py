print('Se quiser parar a digitação informe o número 999')
nume = soma = cont = 0
while nume != 999:
    nume = int(input('Informe um número: '))
    if nume == 999:
        break
    cont += 1
    soma += nume
print(f'Você digitiou {cont} e a soma deles foi {soma}')
