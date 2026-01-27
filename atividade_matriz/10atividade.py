#CRIE UMA MATRIZ QUE REPRESENTE A QUANTIDADE DE PRODUTOS VENDIDOS (2 × 2)
# E OUTRA MATRIZ QUE REPRESENTE O PREÇO DESSES PRODUTOS (2 × 2).
#UTILIZE A MULTIPLICAÇÃO DE MATRIZES PARA GERAR UMA MATRIZ QUE REPRESENTE O VALOR TOTAL DAS VENDAS.
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