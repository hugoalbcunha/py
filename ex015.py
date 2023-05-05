dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
result = (60*dias) + (0.15*km)
print(f'O total a pagar é de R${result:.2f}')