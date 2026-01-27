#CRIE UMA MATRIZ QUE REPRESENTE A QUANTIDADE DE PRODUTOS VENDIDOS (2 × 2)
# E OUTRA MATRIZ QUE REPRESENTE O PREÇO DESSES PRODUTOS (2 × 2).
#UTILIZE A MULTIPLICAÇÃO DE MATRIZES PARA GERAR UMA MATRIZ QUE REPRESENTE O VALOR TOTAL DAS VENDAS.
matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Insira quantidade: ')))
    matriz.append(linha)

matriz2 = []
for i in range(2):
    linha2 = []
    for j in range(2):
        linha.append(int(input('Insira os preços: ')))
    matriz2.append(linha)
for i in range(2):
    for j in range(2):
        matriz[i][j] *= matriz2[i][j]
    print(matriz2[i])