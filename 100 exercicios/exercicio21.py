salário = float(input('Digite seu salário em R$: '))
vendas = float(input('Digite suas vendas em R$: '))
comissão = vendas * 0.04
valor = vendas + comissão
salário_final = salário + valor
print(f'Seu sálario de R$ {salário} + vendas com comissão de 4% de R$ {valor} é igual ao salário final de R$ {salário_final}')