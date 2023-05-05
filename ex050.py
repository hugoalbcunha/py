soma = 0
cont = 0
for i in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 ==0:
        cont = cont + 1
        soma = soma + num
if cont != 1:
    print(f'A soma dos {cont} números pares informados é: {soma}')
else:
    print(f'Somente um número par foi informado e ele é: {soma}')
