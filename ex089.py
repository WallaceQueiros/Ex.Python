ficha = list()
while True:
    nome = str(input('Nome: '))
    nota = float(input('Primeira Nota: '))
    nota2 = float(input('Segunda Nota: '))
    media = (nota + nota2) / 2
    ficha.append([nome, [nota, nota2], media])
    resp = str(input('Quer continuar? [Sim/Não]: ')).strip().upper()
    if resp in 'N':
        break
print('=' * 26)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    print('=' * 26)
while True:
    print('Se não quiser ver nenhuma nota digite -2')
    opc = int(input('Ver nota do aluno N°: '))
    if opc == -2:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
