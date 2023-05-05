nome = input('Digite seu nome completo: ')
tamanho = len(nome.split())
primeiro = nome.split()[0]
ultimo = nome.split()[tamanho-1]
print(f'Nome: {nome}\nPrimeiro: {primeiro}\nUltimo: {ultimo}')

