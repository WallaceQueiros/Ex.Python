lista = list()
listab = list()
listac = list()
while True:
    nume = int(input('Digite um número: '))
    lista.append(nume)
    listab.append(nume)
    opcao = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if nume % 2 != 0:
        listab.remove(nume)
    if nume % 2 != 0:
        listac.append(nume)
    if opcao == 'N':
        break
print(f'Essa é a lista completa: {lista}')
print(f'Essa é a lista de números pares: {listab}')
print(f'Essa é a lista de números impares: {listac}')
