#CRIE DUAS MATRIZES 2 × 2 COM VALORES INFORMADOS PELO USUÁRIO.
#GERE UMA TERCEIRA MATRIZ CONTENDO A SOMA DAS DUAS MATRIZES E MOSTRE O RESULTADO.]

matriza = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Insira um valor: ')))
    matriza.append(linha)
for i in range(2):
    print(matriza[i])

matrizb = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Insira um valor: ')))
    matrizb.append(linha)
for i in range(2):
    print(matrizb[i])

matrizc = []

for i in range(2):
    linha_soma = []
    for j in range(2):
        soma = matriza[i][j] + matrizb[i][j]
        linha_soma.append(soma)
    matrizc.append(linha_soma)

print('Soma das matrizes')
for i in range(2):
    print(matrizc[i])