valo_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos_pagar = int(input('Informe em quantos anos deseja pagar: '))
# Dados do usuario
valor_prestacao = valo_casa / (anos_pagar * 12)
valor_limite = (salario * 30) / 100

# Variaves e recebimento de valores
if valor_prestacao <= valor_limite:
    print(f'O valor da sua prestação será de {valor_prestacao :.2f}, você pode pegar um emprestimo.')
else:
    print('Você não pode fazer um emprestimo, sua prestação excedeu 30% do salário. ')
