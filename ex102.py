def fatorial(numb, show=False):
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
