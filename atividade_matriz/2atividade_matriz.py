# CRIE UMA MATRIZ 3 × 3 JÁ PREENCHIDA COM NÚMEROS INTEIROS DEFINIDOS NO CÓDIGO.
# MOSTRE TODOS OS VALORES DA MATRIZ NA TELA, LINHA POR LINHA.

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz = []

for i in range(3):
    matriz.append(A)
    for j in range(3):
        print(matriz[i][j], end=' ')
    print(matriz)