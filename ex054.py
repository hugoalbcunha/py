"""leia a idadce de sete pessoas e diga
 quantas são de maior e quantas não são"""
import datetime
maior = 0
menor = 0
for i in range(1,8):
    ano = int(input(f'Digite o ano que a {i}ª pessoa nasceu: '))
    idade = datetime.date.today().year - ano
    print(f'{idade} anos')
    if idade > 21:
        maior += 1
    else:
        menor +=1
print(f'MAIORES DE 21 ANOS: {maior}')
print(f'MENORES DE 21 ANOS: {menor}')