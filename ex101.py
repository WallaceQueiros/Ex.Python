def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade <= 16:
        return f'Com {idade} anos, NÃO VOTA.'
    elif 17 >= idade < 18 or idade > 65:
        return f'Com {idade} anos, O VOTO É OPCIONAL.'
    else:
        return f'Com {idade} anos, O VOTO É OBRIGATÓRIO.'


nascimento = int(input('Informe o seu ano de nascimeto: '))
print(voto(nascimento))
