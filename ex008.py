metro = float(input('Informe o valor em metros: '))
cm = metro*100
mm = metro*1000
km = metro*0.001
hm = metro*0.01
dam = metro*0.1
dm = metro*10

print(f'Valor em metros: {metro}\n{km}km\n{hm}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')