"""Faça um programa que leia um ano qualquer
 e mostre se ele é bissexto."""
ano = int(input('Digite um ano: '))
print(ano % 4)
print(ano % 100)
print(ano // 400)
if ((ano % 4) == 0 and (ano % 100) != 0) or (ano % 400) == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')
