from datetime import date

nome_atleta = str(input('Informe o nome do atleta: '))
ano_nascimento = int(input('Informe a data de nascimento do atleta: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos, é um Atleta MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos, é um atleta INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos, é um atleta Junior.')
elif idade == 20:
    print(f'Você tem {idade} anos, é um atleta SÊNIOR.')
else:
    print(f'Você tem {idade} anos, é um atleta MASTER.')
