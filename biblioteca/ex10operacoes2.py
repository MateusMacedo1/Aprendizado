# Separe um programa em dois arquivos: um arquivo contendo apenas funções outro arquivo
# contendo apenas o programa principal
# Utilize importação para que o programa funcione corretamente.

import ex10operacoes as ex10

numero = int(input('Digite um numero: '))
resultado = ex10.raiz(numero)
print(f'O resultado: {resultado}')