media = 0
cont = 0
maior = 0
maisvelho = ''
for i in range(1,5):
    print(f'===== {i}ª PESSOA =====')
    nome = input(f'Nome: ').strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo: [M/F]: ').lower().strip()
    media += idade
    if sexo == 'm':
        if i == 1:
            maior = idade
            maisvelho = nome
        else:
            if idade > maior:
                maior = idade
                maisvelho = nome
    if sexo == 'f':
        if idade < 20:
            cont+=1
print(f"""
A média de idade do grupo é de \033[34m{media/4}\033[m anos
O homem mais velho tem \033[34m{maior}\033[m anos e se chama \033[34m{maisvelho}\033[m
Ao todo são \033[34m{cont}\033[m mulheres com menos de 20 anos
""")