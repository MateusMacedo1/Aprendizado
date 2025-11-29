faturamento = 1200
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas
taxa_imposto = 0.1

mensagem = 'O faturamento foi de 1000'
teve_lucro = False

imposto = taxa_imposto * faturamento

print('faturamento', faturamento)
print('custo', custo)
print('lucro', faturamento - custo)
print(mensagem, faturamento)