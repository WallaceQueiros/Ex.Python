from time import sleep
nume = cont = 0
print('{:=^26}'.format(' TABUADA '))
print('=' * 26)
while True:
    print('Digite qualquer número inteiro negativo para sair do programa.')
    nume = int(input('Digite um número para ver sua tabuada: '))
    if nume < 0:
        break
    while cont < 10:
        cont += 1
        sleep(0.8)
        print(f'{nume} x {cont:2} = {nume * cont}')
    cont = 0

