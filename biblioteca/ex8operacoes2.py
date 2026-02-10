#No arquivo operacoes.py, crie uma função que calcule a soma de dois números.
#Em outro arquivo, importe apenas essa função e utilize-a para somar dois valores digitados pelo usuário.

import ex8operacoes as ex8

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

resultado = ex8.somar(n1, n2)
print(f'O resultado: {resultado}')
