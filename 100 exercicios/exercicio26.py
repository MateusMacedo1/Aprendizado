valor = float(input('Digite o valor do produto: '))
if valor <= 50.00:
    print(f'O valor de venda do seu produto será: {valor + (valor * 0.45)}')
else:
    print(f'O valor de venda de seu produto será: {valor + (valor * 0.30)}')