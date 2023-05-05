"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""
a = float(input('Informe o valor do primeiro lado: '))
b = float(input('Informe o valor do segundo lado: '))
c = float(input('Informe o valor do terceiro lado: '))

if(abs(b-c)<a<b+c) and (abs(a-c)<b<a+c) and(abs(a-b)<c<a+b):
    if a == b == c:
        print(f'É possivel formar um triângulo e ele é Equilátero!')
    elif a != b != c != a:
        print(f'É possivel formar um triângulo e ele é Escaleno!')
    else:
        print(f'É possivel formar um triângulo e ele é Isóceles!')
else:
    print('Não é possivel formar um triângulo.')