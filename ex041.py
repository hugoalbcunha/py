"""
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
import datetime
data = int(input('Informe o ano de nascimento do atleta: '))
ano_hoje = datetime.date.today().year
categoria = ano_hoje - data
print(f'{categoria} anos')
if categoria <= 9 :
    print(f'CATEGORIA: MIRIM')
elif categoria <= 14:
    print(f'CATEGORIA: INFANTIL')
elif categoria <= 19:
    print(f'CATEGORIA: JUNIOR')
elif categoria <= 25:
    print(f'CATEGORIA: SÊNIOR')
else:
    print(f'CATEGORIA: MASTER')