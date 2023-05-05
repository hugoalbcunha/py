"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
valor = float(input('Qual o valor do produto? '))
print('[ 1 ] à vista dinheiro/cheque.')
print('[ 2 ] à vista cartão.')
print('[ 3 ] em até 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
pagamento = input('Informe a forma de pagamento: ')
if pagamento == '1':
    desconto = 10
    valor_final = valor - (valor * desconto / 100)
    print(f'Pagamento à vista em dinheiro/cheque\nDesconto de {desconto}%\nValor final: R${valor_final:.2f}'.replace('.',',').replace('_','.'))
elif pagamento == '2':
    desconto = 5
    valor_final = valor - (valor * desconto / 100)
    print(f'Pagamento à vista cartão\nDesconto de {desconto}%\nValor final: R${valor_final:.2f}'.replace('.',',').replace('_','.'))
elif pagamento == '3':
    desconto = 0
    valor_final = valor - (valor * desconto / 100)
    print(f'Pagamento em 2x no cartão\nSem Juros\n2x R${valor_final/2:.2f}\nValor final: R${valor_final:.2f}'.replace('.',',').replace('_','.'))
elif pagamento == '4':
    desconto = 20
    valor_final = valor + (valor * desconto / 100)
    qparcelas = int(input('Quantas parcelas? '))
    vparcelas = valor_final / qparcelas
    print(f'Pagamento em {qparcelas}x no cartão\nJuros de {desconto}%\n{qparcelas}x R${vparcelas:.2f}\nValor final: R${valor_final:.2f}'.replace('.',',').replace('_','.'))
else:
    print('Opção invalida!')
