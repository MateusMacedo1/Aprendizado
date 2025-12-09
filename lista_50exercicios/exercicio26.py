#Leia uma lista de números inteiros e gere outra lista contendo apenas os números positivos. Exiba ambas as listas.

n = int(input('Quantos números você vai digitar? '))

todos_numeros = []
positivos = []

for i in range(n):
    valor = int(input(f'Digite um número: '))
    todos_numeros.append(valor)

for numero in todos_numeros:
    if numero > 0:
        positivos.append(numero)

print(f'Lista completa: {todos_numeros}')
print(f'Apenas positivos: {positivos}')