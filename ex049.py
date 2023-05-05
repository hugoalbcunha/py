msg = 'TABUADA DO '
numero = int(input('informe um número: '))
print(f'TABUADA DO {numero}')
for i in range(1, 11):
    print(f'{numero: ^2}x {i: ^3}= {numero * i: ^3}')
