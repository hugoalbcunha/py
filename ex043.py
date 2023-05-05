"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
nome = input('Digite seu nome: ')
peso = float(input('Informe seu peso: '))
altura = int(input('Informe sua altura em cm: '))/100
imc = peso/(altura * altura)
if imc < 18.5:
    print(f'Nome: {nome}\nIMC: {imc:.1f}\nAbaixo do Peso.')
elif 18.5 <= imc < 25:
    print(f'Nome: {nome}\nIMC: {imc:.1f}\nPeso ideal.')
elif 25 <= imc < 30:
    print(f'Nome: {nome}\nIMC: {imc:.1f}\nSobrepeso.')
elif 30 <= imc < 40:
    print(f'Nome: {nome}\nIMC: {imc:.1f}\nObesidade.')
elif imc >= 40:
    print(f'Nome: {nome}\nIMC: {imc:.1f}\nObesidade mórbida.')
