"""Escreva um programa que pergunte o salário de um funcionário
 e calcule o valor do seu aumento. Para salários superiores
  a R$1250,00, calcule um aumento de 10%. Para os inferiores
   ou iguais, o aumento é de 15%."""
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    aumento = 10
    nsalario = salario + (salario * aumento/100)
else:
    aumento = 15
    nsalario = salario + (salario * aumento/100)
print(f'O novo salario do funcionário é R${nsalario:.2f} com um aumento de {aumento}%')
