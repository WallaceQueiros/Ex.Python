valores = list()
for cont in range(0, 5):
    nume = int(input('Digite um valor: '))
    if cont == 0 or nume > valores[-1]:
        valores.append(nume)
    else:
        pos = 0
        while pos < len(valores):
            if nume <= valores[pos]:
                valores.insert(pos, nume)
                break
            pos += 1
print(valores)