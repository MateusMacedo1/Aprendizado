carteira = float(input('Digite o valor de sua carteira: '))
dólar = float(input('Digite a cotação do dólar: '))
valor = carteira / dólar
print(f'Com R${carteira:.2f} você pode comprar {valor:.2f} dólares')