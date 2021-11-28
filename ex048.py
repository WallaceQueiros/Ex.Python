'''S = 0
cont = 0
for c in range(1, 501, 2):
    impar = c % 3
    if impar == 0:
        cont += 1
        S += c
print(f'A soma dos {cont} multiplos de 3 vai ser: {S}')'''
S = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        S += c
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {S}')
