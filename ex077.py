palavras = ('aprender', 'programar', 'arroz', 'feijao', 'batata', 'manga', 'fruta', 'suco', 'reservado', 'entrada')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
