#CRIE DUAS MATRIZES 3 × 3 COM VALORES INTEIROS.
#CALCULE E MOSTRE A MATRIZ RESULTANTE DA SOMA, SOMANDO OS VALORES QUE ESTÃO NA MESMA POSIÇÃO.
print('Matriz 1')
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in range(2):
    linha = []
    for j in range(2):
        matriz.append(linha)
for i in range(3):

    print(matriz[i])

print('Matriz 2')

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in range(2):
    linha = []
    for j in range(2):
        matriz2.append(linha)
for i in range(3):

    print(matriz2[i])

matriz3 = []

for i in range(3):
    soma = []
    for j in range(3):
        valor = matriz[i][j] + matriz2[i][j]
        soma.append(valor)
    matriz3.append(soma)

print('Soma da matriz')
for linha in matriz3:
    print(linha)