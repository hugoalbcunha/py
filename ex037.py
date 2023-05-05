num = int(input('Digite um número inteiro: '))
print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
opcao = int(input('Escolha a base de converção do número: '))
if opcao == 1:
    print(f'O número {num} em Binario é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'O nùmero {num} em Octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} em Hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida!')