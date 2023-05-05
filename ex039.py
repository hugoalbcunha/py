"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço
militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
"""
import datetime
ano = int(input('Informe seu ano de nascimento: '))
ano_alista = datetime.date.today().year
idade = ano_alista - ano
sexo = int(input('Qual o seu sexo?\n[ 1 ] Feminino\n[ 2 ] Masculino\n '))
if sexo == 1:
    print('Você não precisa se alistar.')
else:
    if idade < 18:
        print(f'Quem nasceu em {ano} tem {idade} em {ano_alista}')
        print(f'Você ainda vai se alista ao serviço militar em: {18 - idade} ano(s)')
        print(f'Seu alistamento será em {ano_alista + (18 - idade)}')

    elif idade == 18:
        print(f'Quem nasceu em {ano} tem {idade} em {ano_alista}')
        print(f'Esta na hora de você se alistar.')
    else:
        print(f'Quem nasceu em {ano} tem {idade} em {ano_alista}')
        print(f'Você deveria ter se alistado há {idade - 18} ano(s)')
        print(f'Seu alistamento foi em {ano_alista - (idade - 18)}')