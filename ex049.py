from time import sleep

print('{:=^26}'.format(' TABUADA '))
nume = int(input('Informe um número inteiro: '))
print('=' * 26)
for c in range(0, 11):
    sleep(1)
    print(f'{nume} X {c:2} = {nume * c}')
