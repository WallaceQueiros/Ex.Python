expr = str(input('Digite a expressão: '))
lista = list()
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida! ')
else:
    print('Sua expressão é invalida! ')
