valor = float(input('Digite o valor do produto R$: '))
desconto = valor * 0.05
valor_com_desconto = valor - desconto
print(f'Seu produto com desconto está a R$ {valor_com_desconto:.2f}')