p = int(input('Digite a quantidade de camisetas pequenas: '))
m = int(input('Digite a quantidade de camisetas médias: '))
g = int(input('Digite a quantidade de camisetas grandes: '))

print(f'Você comprou a quantidade de: {p + m + g} camisetas\nCamiseta tam. pequena {p} un. valor unitário R$: {p * 10}\nCamiseta tam. media {m} un. valor unitário R$: {m * 12}\nCamiseta tam. grande {g} un. valor unitário R$: {g * 15}\nFicou no total de R$: {(p * 10) + (m * 12) + (g * 15)}')