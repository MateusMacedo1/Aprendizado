#CRIE DUAS MATRIZES 2 × 2 COM VALORES INTEIROS.
#CALCULE A MULTIPLICAÇÃO ENTRE ELAS E MOSTRE A MATRIZ RESULTANTE.

matriz =[
    [1, 2],
    [3, 4]
]
matriz2 = [[1, 2],
           [3, 4]
]

for i in range(2):
    for j in range(2):
        matriz[i][j] *= matriz2[i][j]
    print(matriz[i])