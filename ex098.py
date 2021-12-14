from time import sleep

print('=' * 30)


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for cont in range(inicio, fim, passo):
        print(cont, end=' '), sleep(0.5)
    print('FIM!')
    print('=' * 30)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem! ')
cont_inicio = int(input('Inicio: '))
cont_fim = int(input('Fim: '))
cont_passo = int(input('Passo: '))
print('=' * 30)
contador(cont_inicio, cont_fim, cont_passo)
