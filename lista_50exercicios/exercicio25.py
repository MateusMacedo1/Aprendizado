#Leia uma quantidade n de produtos, com nome e preço, e ao final exiba o total gasto, o produto mais caro e o mais barato.

n = int(input('Quantos produtos você vai cadastrar? '))

nomes = []
precos = []

for i in range(n):

    nome = input('Nome do produto: ')
    preco = float(input('Preço R$: '))
    
    nomes.append(nome)
    precos.append(preco)

total = sum(precos)

maior_preco = max(precos)
posicao_maior = precos.index(maior_preco)
nome_mais_caro = nomes[posicao_maior]

menor_preco = min(precos)
posicao_menor = precos.index(menor_preco)
nome_mais_barato = nomes[posicao_menor]

print(f'Total gasto: R$ {total:.2f}')
print(f'Produto mais caro: {nome_mais_caro} (R$ {maior_preco:.2f})')
print(f'Produto mais barato: {nome_mais_barato} (R$ {menor_preco:.2f})')