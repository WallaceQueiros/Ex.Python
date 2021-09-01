aluno = str(input('Informe seu nome: '))
nota1 = float(input('Informe a primeira nota do Aluno: '))
nota2 = float(input('Informe a segunda nota do Aluno: '))
med = (nota1 + nota2) / 2

print('{} teve as seguintes notas {:.1f} e {:.1f} ficando com uma média de {:.1f}'.format(aluno, nota1, nota2, med))
