import random
import time

segredo = random.randint(0,5)
print('Vou pensar em um número de 0 à 5.')
print(segredo)
num = int(input('Descubra o número escolhido pelo computador: '))
print('PROCESSANDO...')
time.sleep(3)
if num == segredo:
    print('Certa resposta!!!')
else:
    print(f'Que pena, você errou!\nEu pensei no número {segredo}.')