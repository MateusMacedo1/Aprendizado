print('-' *30)
print('Calculo de custo do combustivel')
print('-' *30)

km = int(input('Digite a distância da viajem em quilometros: '))
gas = float(input('Digite o valor da combustivel: '))
print('-' *30)

gasto = gas * km
print(f'Seu gasto de total de combustivel é {gasto:.2f}')