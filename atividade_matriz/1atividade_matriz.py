# CRIE UM PROGRAMA QUE LEIA VALORES INTEIROS PARA PREENCHER UMA MATRIZ 2 × 2.
# DEPOIS DE PREENCHIDA, MOSTRE A MATRIZ NA TELA ORGANIZADA EM LINHAS E COLUNAS.


matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Insira um valor: ')))
    matriz.append(linha)
for i in range(2):

    print(matriz[i])