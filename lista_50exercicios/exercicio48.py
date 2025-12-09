#Leia as vendas diárias de uma semana e exiba o total, a média, o maior e o menor valor, além da lista ordenada.

dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

vendas = []

for dia in dias_semana:
    while True:
        try:
            valor = float(input(f'Valor vendido na {dia}: R$ '))
            
            if valor < 0:
                print('Valor inválido! Não existem vendas negativas.')
            else:
                vendas.append(valor)
                break
        except ValueError:
            print('Digite apenas números.')

total = sum(vendas)
media = total / len(vendas)
maior_venda = max(vendas)
menor_venda = min(vendas)

vendas.sort()

print(f'Total Vendido: R$ {total:.2f}')
print(f'Média Diária: R$ {media:.2f}')
print(f'Melhor Dia: R$ {maior_venda:.2f}')
print(f'Pior Dia: R$ {menor_venda:.2f}')