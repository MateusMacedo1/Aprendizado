# Leia números inteiros até que o usuário digite 0 e ao final exiba a quantidade,
# a soma, a média, o maior e o menor valor.

try:
    
    quant = int(input('Digite a quantidade de nomes deseja inserir: '))

    nomes = []
    for i in range(quant):
        nome = str(input('Digite o nome: ').strip())
        nomes.append(nome)

    if nome:
        nome_maior = max(nomes, key=len)
        nome_menor = min(nomes, key=len)
        print(f'Total de nomes digitados: {len(nomes)}')
        print(f'O maior nome é {nome_maior}, ele possui {len(nome_maior)} caracteres')
        print(f'O menor nome é {nome_menor}, ele possui {len(nome_menor)} caracteres')
    else:
        print('Nomes não digitados')

except ValueError:
    print('Valor incorreto')