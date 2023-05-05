cidade = input('Digite o nome da sua cidade: ').lower()
cid = cidade.split()[0]
if cid == 'santo':
    print('Sua cidade começa com santo')
else:
    print('Sua cidade não começa com santo')