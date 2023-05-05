real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.034739703957305
euro = real / 5.493298176225005
iene = real / 0.0383980340206581
print(f'Com R${real}, você pode comprar:\nU${dolar:.2f}\n€{euro:.2f}\n¥{iene:.2f}')