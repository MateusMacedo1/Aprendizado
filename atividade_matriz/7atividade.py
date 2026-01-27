#CRIE UMA MATRIZ 2 × 2 E UM NÚMERO INTEIRO.
#MULTIPLIQUE TODOS OS VALORES DA MATRIZ POR ESSE NÚMERO E MOSTRE A NOVA MATRIZ.

matriz =[
    [1, 2],
    [3, 4]
]

for i in range(2):
    for j in range(2):
        matriz[i][j] *= 2
    print(matriz[i])