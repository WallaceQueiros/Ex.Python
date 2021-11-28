nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua media foi {media :.1f}, REPROVADO. ')
elif media < 6.9:
    print(f'Sua média foi {media :.1f}, RECUPERAÇÃO. ')
elif media >= 7.0:
    print(f'Sua média foi {media :.1f}, APROVADO. ')
