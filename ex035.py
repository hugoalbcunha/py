"""Desenvolva um programa que leia o comprimento de 3 retas
 e diga ao usuário se elas podem ou não formar um triângulo"""
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if (abs(b-c)<a<b+c) and (abs(a-c)<b<a+c) and(abs(a-b)<c<a+b):
    print(f'Dado as retas de comprimento {a},{b},{c}, é possível formar um triângulo')
else:
    print(f'Dado as retas de comprimento {a},{b},{c}, não é possível formar um triângulo')