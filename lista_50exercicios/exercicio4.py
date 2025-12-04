# Leia um número inteiro e informe se ele é positivo, negativo ou zero.
try:

    num = int(input('Digite um numero: '))

    if num < 0:
        print('Negativo')
    elif num == 0:
        print('Zero')
    else:
        print('Positivo')

except ValueError:
    print('ERRO')