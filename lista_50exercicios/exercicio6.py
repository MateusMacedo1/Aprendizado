# Leia a temperatura em Celsius e informe se o clima está frio, agradável ou quente.
temp = int(input('Digite a temperatura em Celsius: '))
if temp <= 15:
    print('Clima Frio')
elif temp > 15 and temp < 25:
    print('Clima Agradável')
else:
    print('Clima Quente')