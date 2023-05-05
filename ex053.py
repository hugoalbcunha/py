'Programa para verificar se uma frase é palíndromo'
inverso = ''
frase = input('Digite uma frase: ').strip().replace(" ", "").upper()
for i in range(0, len(frase)):
    compara = len(frase) - i
    inverso += frase[compara-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é palíndromo')