from datetime import date

# menu
print('=' * 31)
print('Serviço de Alistamento Militar')
print('=' * 31)
# Tela cadastro
cadastro_nome = str(input('Informe o seu nome: '))
cadastro_nasci = int(input('Informe sua data de nascimento: '))
idade = date.today().year - cadastro_nasci
tempo_alista = 18 - idade
tempo_passou = idade - 18

# funcionalidade
if idade == 18:
    print(f'Sua idade é {idade} anos está na hora de se alistar.')
    print('Venha fazer parte das Forças Armadas Brasileira. ')
elif idade < 18:
    print(f'Sua idade é {idade} anos, não é necessário se alistar.')
    print(f'Faltam {tempo_alista} ano(s) para você se alistar. ')
elif idade >= 19:
    print(f'Sua idade é {idade} anos, já passou da hora de se alistar.')
    print(f'Já se passou {tempo_passou} ano(s), alistesse já. ')
