#Crie um programa que importe as bibliotecas math e random e utilize uma função de cada
# uma para gerar um número aleatório e calcular sua raiz quadrada.

import random
numero = random.randint(1, 100)

import math
raiz = math.sqrt(numero)

print(f'Número aleatório é: {numero} e sua Raiz quadrada: {raiz:.2f}')