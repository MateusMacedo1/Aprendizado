#Leia vários números até que o usuário digite uma palavra-chave para encerrar. Ao final, exiba a quantidade, soma, média, maior e menor valor.
numeros = []

print("Digite 'fim' para encerrar e ver o relatório.")

while True:
    entrada = input('Digite um número: ')
    
    if entrada.lower() == 'fim':
        break
    
    try:
        valor = float(entrada)
        numeros.append(valor)
    except ValueError:
        print('Entrada inválida!')

if len(numeros) > 0:
    qtd = len(numeros)
    soma = sum(numeros)
    media = soma / qtd
    maior = max(numeros)
    menor = min(numeros)
    
    print(f'Quantidade de números: {qtd}')
    print(f'Soma total: {soma:.2f}')
    print(f'Média dos valores: {media:.2f}')
    print(f'Maior valor digitado: {maior}')
    print(f'Menor valor digitado: {menor}')

else:
    print('\nNenhum número foi digitado.')