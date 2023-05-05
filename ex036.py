"""Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador
 e em  quantos anos ele vai pagar. A prestação mensal não pode
 exceder 30% do salário ou então o empréstimo será negado."""
import time
valor = float(input('Qual o valor da casa que o Sr quer financiar? '))
salario = float(input('Qual o valor do seu salário? '))
quantidade = int(input('Quanto anos de financiamento? '))
prestacao = valor/(quantidade*12)
limite = salario * (30/100)
print('FAZENDO A SIMULAÇÃO...')
if prestacao <= limite :
    time.sleep(1)
    print(f'VALOR FINANCIADO: R${valor:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'RENDA: R${salario:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'Nº DE PRESTAÇÕES: {quantidade*12} vezes.({quantidade} anos)')
    time.sleep(1)
    print(f'VALOR DA PRESTAÇÃO: R${prestacao:_.2f}'.replace('.', ',').replace('_', '.'))
    time.sleep(1)
    print(f'LIMITE DE RENDA: R${limite:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'SEU FINANCIAMENTO SERÁ APROVADO!')
else:
    time.sleep(1)
    print(f'VALOR FINANCIADO: R${valor:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'RENDA: R${salario:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'Nº DE PRESTAÇÕES: {quantidade*12} vezes.({quantidade} anos)')
    time.sleep(1)
    print(f'VALOR DA PRESTAÇÃO: R${prestacao:_.2f}'.replace('.', ',').replace('_', '.'))
    time.sleep(1)
    print(f'LIMITE DE RENDA: R${limite:_.2f}'.replace('.',',').replace('_','.'))
    time.sleep(1)
    print(f'SEU FINANCIAMENTO \033[7mNÃO\033[m SERÁ APROVADO!')