nume1 = int(input('Informe o primeiro número: '))
nume2 = int(input('Informe o segundo número: '))
nume3 = int(input('Informe o terceiro número: '))
# Verificar o maior
maior = nume1
if nume2 > nume1 and nume2 > nume3:
    maior = nume2
if nume3 > nume1 and nume3 > nume2:
    maior = nume3
# Verificar o menor
menor = nume1
if nume2 < nume1 and nume2 < nume3:
    menor = nume2
if nume3 < nume1 and nume3 < nume2:
    menor = nume3

print('O maior número informado é: {}'.format(maior))
print('O menor número informado é: {}'.format(menor))
