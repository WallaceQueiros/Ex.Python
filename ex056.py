soma_idade = 0
idade_media = 0
idade_hvelho = 0
nome_hvelho = ''
idade_mulher = 0
for c in range(1, 5):
    nome = str(input(f'Informe o nome da {c}° pessoa: ')).strip()
    idade = int(input(f'Informe a idade da {c}° pessoa: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    idade_media = soma_idade / 4
    if c == 1 and sexo in 'M':
        idade_hvelho = idade
        nome_hvelho = nome
    if sexo in 'M' and idade > idade_hvelho:
        idade_hvelho = idade
        nome_hvelho = nome
    if sexo in 'F' and idade < 20:
        idade_mulher += 1
print(f'A média de idade do grupo é de {idade_media:.1f}')
print(f'O homem mais velho se chama {nome_hvelho}, e tem {idade_hvelho} anos.')
print(f'E se tem {idade_mulher} mulheres com menos de 20 anos. ')
