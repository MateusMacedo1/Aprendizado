dia = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos km o carro rodou: '))
pdia = 60 * dia
kmr = km * 0.15
print(f'O Carro alugado por {dia} dias rodou {km} km e o valor a pagar foi de R$: {pdia + kmr:.2f}')