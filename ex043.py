# Informações Usuario
peso_usu = float(input('Informe o peso do paciente em Kg: '))
altura_usu = float(input('Informe a altura do paciente em metros: '))
imc_usu = peso_usu / (altura_usu ** 2)
# Condições
if imc_usu < 18.5:
    print(f'Seu IMC é de {imc_usu :.2f}, você está Abaixo do Peso. ')
elif imc_usu <= 25:
    print(f'Seu IMC é {imc_usu :.2f}, você está no Peso Ideal. ')
elif imc_usu <= 30:
    print(f'Seu IMC é de {imc_usu :.2f} , você está na faixa de SOBREPESO. ')
elif imc_usu <= 40:
    print(f'Seu IMC é de {imc_usu :.2f}, você está na faixa de OBESIDADE')
elif imc_usu > 40:
    print(f'Seu IMC é de {imc_usu :.2f}, você está na faixa de OBESIDADE MÓRBIDA.')
