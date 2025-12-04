# Leia altura e peso, calcule o IMC e classifique o resultado de acordo com as categorias estabelecidas.

try:
    alt = float(input('Digite a altura em mts: '))
    peso = float(input('Digite o peso em kg: '))

    valor = peso / (alt * alt)

    if valor >= 0 and valor <= 18.5:
        print(f'Se um imc é {valor:.1f} você está abaixo do peso')
    elif valor > 18.5 and valor <= 24.9:
        print(f'Se um imc é {valor:.1f} você está com peso normal')
    elif valor > 24.9 and valor <= 29.9:
        print(f'Se um imc é {valor:.1f} você está com sobrepeso')
    elif valor > 29.9:
        print(f'Se um imc é {valor:.1f} você está obeso')
    else:
        print('Valores incorretos')
except ValueError:
    print('Dado incorreto')