import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.sqrt(math.pow(co, 2)+math.pow(ca, 2))
print(f'A hipotenusa desse triângulo vale: {h}')
