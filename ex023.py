num = int(input('Digite um número de 0 à 9999: '))
'''
if (int(num) >= 0 and int(num)<= 9999 and len(num)==4):
    print(f'Unidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')
else:
    print('Número digitado inválido')
'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')