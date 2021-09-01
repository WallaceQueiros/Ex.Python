'''frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'{junto} - {inverso}')
    print('A frase digitada é um palíndromo.')
else:
    print(f'{junto} - {inverso}')
    print('A frase digitada não é um palindromo.')'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print(f'{junto} - {inverso}')
if inverso == junto:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada não é um PALÍNDROMO.')
