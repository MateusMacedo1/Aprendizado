# Leia o valor de um produto e o tipo de pagamento
# (1 para à vista, 2 para cartão, 3 para boleto)
# e calcule o valor final considerando regras diferentes para cada forma de pagamento.
try:
    valor = float(input('Digite o valor do Produto: '))
    pag = int(input('Digite a forma de pagamentos: '))

    avista = valor
    cartão = (valor + (valor * 0.10))
    boleto = (valor + (valor * 0.05))

    if pag == 1:
        print(f'Seu valor final é {avista}')
    elif pag == 2:
        print(f'Seu valor final é {cartão}')
    elif pag == 3:
        print(f'Seu valor final é {boleto}')
    else:
        print('Forma de pagemento inválido')
except ValueError:
    print('Valor inválido')