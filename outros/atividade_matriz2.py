
matriz = []

print(matriz)

for i in range(5):
    linha = []
    for j in range(3):
        if i == 0:
            linha.append(j)
        elif j == 0:
            linha.append(i)
        else:
            linha.append(i * j)
    matriz.append(linha)

for i in range(5):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print('\n')