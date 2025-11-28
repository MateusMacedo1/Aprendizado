salário = float(input('Digite o salário para saber o reajuste R$: '))

if salário > 0 and salário <= 280.00:
    print(f'Seu salário de {salário} teve reajuste de 20%, passa a ser agora R$: {salário + (salário * 0.20)}')
elif salário > 280.00 and salário <= 700.00:
    print(f'Seu salário de {salário} teve reajuste de 15%, passa a ser agora R$: {salário + (salário * 0.15)}')
elif salário > 700.00 and salário <= 1500.00:
    print(f'Seu salário de {salário} teve reajuste de 10%, passa a ser agora R$: {salário + (salário * 0.10)}')
else:
    print(f'Seu salário de {salário} teve reajuste de 5%, passa a ser agora R$: {salário + (salário * 0.05)}')