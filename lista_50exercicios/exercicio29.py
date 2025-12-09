#Leia um número inteiro n e calcule o fatorial de n.

n = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

for i in range(1, n + 1):
    fatorial = fatorial * i

print(f'O fatorial de {n} é {fatorial}')