#Crie um programa que importe apenas a função de potência da biblioteca math
# e utilize essa função para calcular a potência de dois números digitados pelo usuário.
import math
numero = int(input('Digite um numero para calcular a sua potencia: '))
expoente = int(input('Digite um numero do seu expoente: '))

print(f'A potencia do numero {numero} é: {math.pow(numero, expoente)}')