class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def aumentar(num=0, taxa=0, formato=False):
    numb = num + (num * taxa / 100)
    return numb if formato is False \
        else moedas(numb)


def diminuir(num=0, taxa=0, formato=False):
    numb = num - (num * taxa / 100)
    return numb if formato is False \
        else moedas(numb)


def metade(num=0, formato=False):
    numb = num / 2
    return numb if formato is False \
        else moedas(numb)


def dobro(num=0, formato=False):
    numb = num * 2
    return numb if formato is False \
        else moedas(numb)


def moedas(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')


def resumo(num=0, taxa_alt=0, taxa_min=0):
    print(color.BOLD + '-' * 30 + color.END)
    print(color.BOLD + 'RESUMO VALOR'.center(30) + color.END)
    print(color.BOLD + '-' * 30 + color.END)
    print(f'Preço analisado: \t{moedas(num)}')
    print(f'{taxa_alt}% de aumento: \t{aumentar(num, taxa_alt, True)}')
    print(f'{taxa_min}% de aumento: \t{aumentar(num, taxa_min, True)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Dobro do preço: \t{metade(num, True)}')
    print(color.BOLD + '-' * 30 + color.END)
