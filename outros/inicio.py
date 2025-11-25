altura = int(input('Digite a altura em centimetros: '))
if altura <= 150:
    print('ruim')
elif altura > 150 and altura <= 160:
    print('aceitável')
elif altura > 160 and altura <= 165:
    print('Bom')
elif altura > 165 and altura <= 170:
    print('excelente')
elif altura > 170 and altura <= 175:
    print('bom')
elif altura > 175 and altura <= 180:
    print('aceitavel')
else:
    print('ruim')

peso = int(input('Digite o peso: '))
if peso <= 45:
    print('ruim')
elif peso > 45 and peso <= 55:
    print('Bom')
elif peso > 55 and peso <= 75:
    print('excelente')
elif peso > 75 and peso <= 80:
    print('bom')
else:
    print('ruim')