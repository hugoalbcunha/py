"""Desenvolva um programa que pergunte a distância de uma viagem
 em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
  viagens de até 200Km e R$0,45 parta viagens mais longas."""
dist = float(input('Qual a distancia da sua viagem em Km: '))
preco = 0
if dist <= 200:
    preco = dist*0.50
else:
    preco = dist*0.45
print(f'O valor da viagem de {dist}Km é R${preco:.2f}')