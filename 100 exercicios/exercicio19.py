l1 = float(input('Digite o comprimento de um lado do triangulo: '))
l2 = float(input('Digite o comprimento de um lado do triangulo: '))
l3 = float(input('Digite o comprimento de um lado do triangulo: '))

if l1 == l2 == l3:
    print('Seu triangulo é um equilátero')
elif l1 > l2 == l3 or l1 < l2 == l3 or l1 == l2 < l3 or l1 == l2 > l3 or l2 > l1 == l3 or l2 < l1 == l3:
    print('Seu triangulo é isósceles')
else:
    print('Seu triangulo é escaleno')

