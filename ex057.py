respM = 'M'.upper()[0]
respF = 'F'.upper()[0]
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo != respM and sexo != respF:
    sexo = str(input('Informe seu sexo, novamente: [M/F] ')).strip().upper()[0]
print(f'Seu sexo é {sexo}')
