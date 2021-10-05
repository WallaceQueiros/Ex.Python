valores = list()
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
    else:
        print('O número informado já existe na lista, tente outro.')
    pergunta = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
valores.sort()
print(valores)
