num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    number = int(input('Informe um número entre 0 a 10: '))
    print(f'O número digitado foi {num[number]}')
    if 0 <= number <= 10:
        break
print('Volte sempre')
