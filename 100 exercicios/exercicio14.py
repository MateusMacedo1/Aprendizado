num = int(input('Digite o numero da conta: '))
saldo = float(input('Digite seu saldo em R$: '))
deb = float(input('Digite um débito em R$: '))
cre = float(input('Digite um crédito em R$: '))

saldo_atual = saldo - (deb + cre)

if saldo_atual < 0:
    print(f'Seu saldo é {saldo_atual} negativo')
else:
    print(f'Seu saldo é {saldo_atual} positivo')