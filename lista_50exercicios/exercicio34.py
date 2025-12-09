#Simule um caixa de lanchonete que leia o código de um produto, a quantidade e exiba o nome do item e o valor total.

print('--- SISTEMA CACHORRO QUENTE ---')
print('Código do cachorro quente: 10')
print('Preço: R$ 15.00')

codigo = int(input('\nDigite o código do produto: '))

if codigo == 10:
    quantidade = int(input('Digite a quantidade: '))
    
    preco = 15.00
    total = preco * quantidade
    
    print(f'\nProduto: Cachorro Quente')
    print(f'Valor total a pagar: R$ {total:.2f}')

else:
    print('Código inválido. Nós só vendemos Cachorro Quente (Código 10).')