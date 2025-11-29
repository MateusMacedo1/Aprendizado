Capital = (float(input('Digite o quanto ele vai pegar: ')))

juros = 0.15
tempo_anos = 5
valor_final = Capital * (1 + juros) ** tempo_anos

print(valor_final > 1000000)