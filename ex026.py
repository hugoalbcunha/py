frase = input('Digite uma frase: ').lower().strip()
letra = frase.count('a')
primeira = frase.find('a')+1
ultima = frase.rfind('a')+1
print(f'A letra "a" aparece {letra} vezes\nEla aparece primeiro na posição {primeira}, e por ultimo na posição {ultima}')