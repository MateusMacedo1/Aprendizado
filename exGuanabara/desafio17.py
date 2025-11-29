from math import hypot

opo = float(input('Digite o cateto oposto do triangulo: '))
adj = float(input('Digite o cateto adjacente do triangulo: '))

h = hypot(opo, adj) # hypot é usado para calcular a hipotenusa

print(f'A hipotenusa vai medir: {h:.2f}')