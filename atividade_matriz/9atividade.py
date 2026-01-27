#CRIE DUAS MATRIZES COMPATÍVEIS PARA MULTIPLICAÇÃO (2 × 3 E 3 × 2).
#CALCULE E MOSTRE A MATRIZ RESULTANTE DA MULTIPLICAÇÃO.

matriz =[
    [1, 2, 3],
    [4, 5, 6]
]
matriz2 = [
        [1, 2],
        [3, 4],
        [5, 6]
]

for i in range(2):
    for j in range(2):
        matriz[i][j] *= matriz2[i][j]
    print(matriz[i])