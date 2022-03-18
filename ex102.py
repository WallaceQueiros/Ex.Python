def fatorial(numb, show=False):
    """
    Calcula o fatorial de um número.
    :param numb: Número a ser calculado.
    :param show: mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    """
    f = 1
    for c in range(numb, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


number = int(input('Digite um número inteiro para ser fatorado: '))
print(fatorial(number, show=False))
