maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
        print(f'maior: {maior} | menor: {menor}')
    else:
        if peso < menor:
            menor = peso
            print(f'maior: {maior} | menor: {menor}')
        if peso > maior:
            maior = peso
            print(f'maior: {maior} | menor: {menor}')
        if menor < peso < maior:
            print(f'maior: {maior} | menor: {menor}')
print(f'O maior peso foi: {maior}Kg')
print(f'O menor peso foi: {menor}Kg')