print(f'='*31)
print('{: ^31}'.format('CALCULO DE P.A.'))
print(f'='*31)
termo = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
for termo in range (termo,termo+(10-1)*razao+razao,razao):
    print(termo, end= ' → ')
print('ACABOU')