# Leia o salário bruto de um funcionário
# e calcule o salário líquido com base em regras de desconto por faixa salarial.
try:
    salário = float(input('Digite o valor do seu salário R$: '))

    sind = (salário * 0.03)
    FGTS = (salário * 0.11)
    IR1 = (salário * 0.05)
    IR2 = (salário * 0.10)
    IR3 = (salário * 0.20)
    INSS = (salário * 0.10)


    if salário > 0 and salário <= 900:
        print(f'Salário bruto do mês R$: {salário} \n (-) Sindicato - 3%: {sind} \n (-) FGTS - 11%: {salário + FGTS} \n (-) INSS - 10%: {INSS} \n Salário Liquido R$: {salário - sind - INSS}')
    elif salário > 900 and salário <= 1500:
        print(f'Salário bruto do mês R$: {salário} \n (-) Sindicato - 3%: {sind} \n (-) FGTS - 11%: {salário + FGTS} \n (-) INSS - 10%: {INSS} \n (-) IR - 5%: {IR1} \n Salário Liquido R$: {salário - sind - INSS - IR1}')
    elif salário > 1500 and salário <= 2500:
        print(f'Salário bruto do mês R$: {salário} \n (-) Sindicato - 3%: {sind} \n (-) FGTS - 11%: {salário + FGTS} \n (-) INSS - 10%: {INSS} \n (-) IR - 10%: {IR2} \n Salário Liquido R$: {salário - sind - INSS - IR2}')
    elif salário > 2500:
        print(f'Salário bruto do mês R$: {salário} \n (-) Sindicato - 3%: {sind} \n (-) FGTS - 11%: {salário + FGTS} \n (-) INSS - 10%: {INSS} \n (-) IR - 20%: {IR3} \n Salário Liquido R$: {salário - sind - INSS - IR3}')
    else:
        print('Valor Inválido')
except ValueError:
    print('Dado inválido')