# CRIE UMA MATRIZ QUE REPRESENTE A QUANTIDADE DE PRODUTOS VENDIDOS (2 × 2) E OUTRA MATRIZ QUE REPRESENTE O PREÇO DESSES PRODUTOS (2 × 2).
# UTILIZE A MULTIPLICAÇÃO DE MATRIZES PARA GERAR UMA MATRIZ QUE REPRESENTE O VALOR TOTAL DAS VENDAS
# produto = [
#     [1, 2],
#     [3, 4]
# ]

# preço = [
#     [1, 2],
#     [3, 4]
# ]

# for i in range(2):
#     for j in range(2):
#         produto[i][j] *= preço[i][j]
#     print(produto[i])




produto = [
    [1, 2],
    [3, 4]
]

preço = [
    [1, 2],
    [3, 4]
]

for i in range(2):
    for j in range(2):
        produto[i][j] *= preço[i][j]
    print(produto[i])