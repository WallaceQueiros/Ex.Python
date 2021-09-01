from datetime import date
tot = 0
cont = 0
for c in range(1, 8):

    ano_nasci = int(input(f"Em que ano a {c}° pessoa nasceu: "))
    idade = date.today().year - ano_nasci
    if idade >= 18:
        cont += 1
    elif idade < 18:
        tot += 1
print(f'{cont} Pessoas são maiores de 18 anos. ')
print(f'{tot} Pessoas são menores de 18 anos. ')
