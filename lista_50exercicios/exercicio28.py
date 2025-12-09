#Leia uma quantidade n de valores inteiros e exiba apenas aqueles que forem múltiplos de 3.
n = int(input('Quantos números você vai digitar? '))

numeros = []

for i in range(n):
    valor = int(input(f'Digite o {i+1}º valor: '))
    numeros.append(valor)


encontrou_algum = False

for numero in numeros:
    if numero % 3 == 0:
        print(numero)
        encontrou_algum = True

if encontrou_algum == False:
    print('Nenhum múltiplo de 3 foi encontrado.')