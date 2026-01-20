# Hotel do Thor
matriz = []

for i in range(3):
    linha = []
    for j in range(1):
        if j == 0:
            linha.append(input('Digite o cpf: '))
        elif j == 1:
            linha.append(input('Digite o nome: '))
        elif j == 2:
            linha.append(input('Digite a idade: '))
        else:
            linha.append(input('Digite o quarto: '))
    matriz.append(linha)

for i in range(3):
    for j in range(1):
        print(matriz[i][j], end=' ')
    print('\n')