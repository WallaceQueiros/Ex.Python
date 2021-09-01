'''S = 0
for c in range(1, 7):
    nume = int(input(f'Digite o {c}° valor: '))
    if nume % 2 == 0:
        S += nume

print(f'A soma dos números pares é: {S}')'''
S = 0
cont = 0
for c in range(1, 7):
    nume = int(input(f'Digite o {c}° número: '))
    if nume % 2 == 0:
        S += nume
        cont += 1
print(f'Você digitou {cont} números pares e a soma deles foi: {S}')
