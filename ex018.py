import math
ang = float(input('Informe um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'sen({ang}) = {sen:.2f}\ncos({ang}) = {cos:.2f}\ntan({ang}) = {tan:.2f}')
