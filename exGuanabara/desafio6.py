# Faça um programa que leia um numero em mostre o dobro, triplo e a raiz quadrada

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é {d}. O triplo de {n} é {t}. A raiz quandrada de {n} é {r:.2f}')
# Para realizar a raiz quadrada se utiliza 0.5 ou (1/2) que a raiz é sempre a metade do exponencial
# o uso de :.2f é usado para formatação que pode ser limitada por cada casa no exemplo acima limitei em 2 casas após o ponto