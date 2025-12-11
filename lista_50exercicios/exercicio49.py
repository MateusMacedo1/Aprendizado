#Leia uma lista de produtos com nome e preço e exiba o produto mais caro,
# o mais barato, o preço médio e a lista ordenada pelo nome.

produtos = []

print('Digite fim no nome para encerrar.')

while True:
    nome = input('\nNome do produto: ').strip().title()
    
    if nome.lower() == 'fim':
        break
    
    try:
        preco = float(input(f'Preço do {nome}: R$ '))
        
        produtos.append([nome, preco])
        
    except ValueError:
        print('Erro: Preço inválido. Tente novamente.')

if len(produtos) > 0:
    
    mais_caro = produtos[0]  
    mais_barato = produtos[0]
    soma_precos = 0
    
    for produto in produtos:
        preco_atual = produto[1]
        
        soma_precos = soma_precos + preco_atual
        
        if preco_atual > mais_caro[1]:
            mais_caro = produto
            
        if preco_atual < mais_barato[1]:
            mais_barato = produto
            
    media = soma_precos / len(produtos)
    
    produtos.sort()

    print(f'Preço Médio: R$ {media:.2f}')
    print(f'Produto + Caro: {mais_caro[0]} (R$ {mais_caro[1]:.2f})')
    print(f'Produto + Barato: {mais_barato[0]} (R$ {mais_barato[1]:.2f})')
    
    for p in produtos:
        print(f'-> {p[0]:.<20} R$ {p[1]:.2f}')

else:
    print('Nenhum produto cadastrado.')