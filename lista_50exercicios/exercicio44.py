#Leia uma frase, converta-a para maiúsculas, remova espaços nas extremidades
# e exiba a quantidade de caracteres antes e depois da remoção.

frase_original = input('Digite uma frase: ')

tamanho_antes = len(frase_original)

frase_tratada = frase_original.upper().strip()

tamanho_depois = len(frase_tratada)

print(f'Frase Original: {frase_original}')
print(f'Tamanho Antes:  {tamanho_antes} caracteres')
print(f'Frase corrigida:  {frase_tratada}')
print(f'Tamanho Depois: {tamanho_depois} caracteres')
print(f'Espaços removidos: {tamanho_antes - tamanho_depois}')