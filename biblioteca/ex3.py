#Crie um programa que importe a biblioteca math usando um apelido
# e utilize esse apelido para calcular o valor absoluto de um número negativo.
import math as a
numero = int(input('Digite um numero negativo para saber seu valor absoluto: '))
if numero >= 0: 
    print(f'O valor incorrero! Digite um numero negativo')
else:
    print(f'O valor absoluto do numero {numero} é: {a.fabs(numero)}')
