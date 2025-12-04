# Leia o valor de um produto e o tipo de pagamento
# (1 para à vista, 2 para cartão, 3 para boleto)
# e calcule o valor final considerando regras diferentes para cada forma de pagamento.

valor = float(input('Digite o valor do Produto: '))
avista = (valor - (valor * 0.05))
cartão = (valor + (valor * 0.10))
boleto = (valor + (valor * 0.05))