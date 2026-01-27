#3. CRIE UM PROGRAMA QUE PERGUNTE AO USUÁRIO O NÚMERO DE LINHAS E COLUNAS DE UMA MATRIZ.
# EM SEGUIDA, LEIA OS VALORES E MOSTRE A MATRIZ FORMADA.
lin = int(input('Digite a Quantidade de linha: '))
colu = int(input('Digite a Quantidade de coluna: '))
matriz = []

for i in range(lin):
    linha = []
    for j in range(colu):
        linha.append(int(input('Insira um valor: ')))
    matriz.append(linha)
for i in range(lin):

    print(matriz[i])