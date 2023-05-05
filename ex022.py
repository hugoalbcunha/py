nome = input('Digite seu nome completo: ')
#todas as letras em maiúsculo
print(nome.upper())
#todas as letras em minúsculo
print(nome.lower())
#quantas letras sem espaços
letras = nome.split()
tamanho=0
for i in range (len(letras)):
    tamanho += len(nome.split()[i])
print(f'O nome tem {tamanho} letras')
#quantas letras primeiro nome
print(f'O primeiro nome {letras[0]} tem {len(letras[0])} letras')