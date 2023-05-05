"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import  random
computador = random.randrange(1,3)
print(computador)
print('Vamos jogar Jokenpô!!!!!')
print('[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ]TESOURA')
escolha = ['','PEDRA','PAPEL','TESOURA']
player = int(input('Escolha uma jogada: '))
if escolha[player] == escolha[computador]:
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nEmpate!')
elif escolha[player] == 'PEDRA' and escolha[computador] == 'TESOURA':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Player!')
elif escolha[player] == 'PEDRA' and escolha[computador] == 'PAPEL':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Computador!')
elif escolha[player] == 'TESOURA' and escolha[computador] == 'PAPEL':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Player!')
elif escolha[player] == 'TESOURA' and escolha[computador] == 'PEDRA':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Computador!')
elif escolha[player] == 'PAPEL' and escolha[computador] == 'PEDRA':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Player!')
elif escolha[player] == 'PAPEL' and escolha[computador] == 'TESOURA':
    print(f'Player x Computador\n{escolha[player]} X {escolha[computador]}\nVitória Computador!')