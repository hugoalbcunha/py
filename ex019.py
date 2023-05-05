import random

a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1, a2, a3, a4]
s = random.randint(0, 3)
print(f'O aluno escolhido é: {lista[s]}')
