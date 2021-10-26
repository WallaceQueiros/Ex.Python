aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome: {aluno["nome"]}\nMédia: {aluno["media"]}')
if aluno['media'] < 6:
    print(f' Situação do aluno {aluno["nome"]}é REPROVADO!')
else:
    print(f'Situação do aluno {aluno["nome"]}é APROVADO!')