# Matrizes A e B
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Matrizes C e D
C = [
    [13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22]
]

D = [
    [23, 24],
    [25, 26],
    [27, 28],
    [29, 30],
    [31, 32]
]

# -------------------------
# Multiplicação A x B
# -------------------------
matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        soma = 0
        for k in range(3):
            soma += A[i][k] * B[k][j]
        linha.append(soma)
    matriz.append(linha)

print("A x B =", matriz)

# -------------------------
# Multiplicação C x D
# -------------------------
matriz2 = []

for i in range(2):
    linha = []
    for j in range(2):
        soma = 0
        for k in range(5):
            soma += C[i][k] * D[k][j]
        linha.append(soma)
    matriz2.append(linha)

print("C x D =", matriz2)

# -------------------------
# Soma válida (A + A)
# -------------------------
matrizr = []

for i in range(2):
    linha = []
    for j in range(3):
        linha.append(A[i][j] + A[i][j])
    matrizr.append(linha)

print("A + A =", matrizr)
