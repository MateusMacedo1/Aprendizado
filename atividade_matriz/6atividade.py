#CRIE DUAS MATRIZES 2 × 3 PREENCHIDAS PELO USUÁRIO.
#UTILIZE LAÇOS DE REPETIÇÃO PARA GERAR UMA TERCEIRA MATRIZ COM A SOMA DAS DUAS.

matriza = []

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input('Insira um valor: ')))
    matriza.append(linha)
for i in range(2):
    print(matriza[i])

matrizb = []

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(int(input('Insira um valor: ')))
    matrizb.append(linha)
for i in range(2):
    print(matrizb[i])

matrizc = []

for i in range(2):
    linha_soma = []
    for j in range(3):
        soma = matriza[i][j] + matrizb[i][j]
        
        if soma > 0:
            linha_soma.append(soma)
        else:
            linha_soma.append(0)
            
    matrizc.append(linha_soma) 

print('Soma das matrizes')
for i in range(2):
    print(matrizc[i])