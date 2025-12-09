# Leia números inteiros até que o usuário digite 0 e ao final exiba a quantidade,
# a soma, a média, o maior e o menor valor.

numeros = []

print('Digite números inteiros. Digite 0 para encerrar.')

while True:
    try:
        valor = int(input('Digite um número: '))
        
        if valor == 0:
            break
        
        numeros.append(valor)
        
    except ValueError:
        print('Erro: Digite apenas números inteiros!')

if len(numeros) > 0:
    
    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade
    maior = max(numeros)
    menor = min(numeros)
    
    print(f'Quantidade: {quantidade}')
    print(f'Soma total: {soma}')
    print(f'Média: {media:.2f}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    
else:
    print('\nNenhum número foi digitado antes do zero.')