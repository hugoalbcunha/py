num = int(input('Digite um número inteiro: '))
primo = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[31m', end = ' ')
        primo +=1
    else:
        print('\033[34m', end = ' ')
    print(f'{i}',end = ' ')
if primo == 2:
    print(f'\033[34m\n{num} É um número primo!')
else:
    print(f'\033[m\n{num} \033[31mNÃO\033[m é um número primo.')