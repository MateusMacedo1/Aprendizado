# Leia um número inteiro positivo e exiba todos os números de 1 até ele, além da soma total desses valores.
try:
    num = int(input('Digite um numero inteiro positivo: ')) + 1
    for i in range(0, num):
        print(i)
except ValueError:
    print('Somente numeros inteiros positivos')
