soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        cont = cont +1
        soma = soma+i
print(f'A soma dos {cont} valores impares míltiplos de 3 entre 1 e 500 é {soma}')