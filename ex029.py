"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada
Km acima do limite.
"""
import time
kmh = float(input('Informe a velocidade do carro: '))
print('O limite de velocidade é 80km/h')
if kmh >80:
    multa = (kmh-80)*7
    print(f'Você está à {kmh}km/h')
    time.sleep(1)
    print('PROCESSANDO...')
    time.sleep(3)
    print('MULTADO!')
    time.sleep(2)
    print(f'Valor da multa: R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')