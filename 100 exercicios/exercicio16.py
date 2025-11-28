num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
num3 = int(input('Digite mais outro numero: '))

if num1 > num2 > num3:
    print(f'{num3} é o menor e {num1} é o maior')
elif num1 > num3 > num2:
    print(f'{num2} é o menor e {num1} é o maior')
elif num2 > num1 > num3:
    print(f'{num3} é o menor e {num2} é o maior')
elif num2 > num3 > num1:
    print(f'{num1} é o menor e {num2} é o maior')
elif num3 > num1 > num2:
    print(f'{num2} é o menor e {num3} é o maior')


elif num3 > num2 > num1:
    print(f'{num1} é o menor e {num3} é o maior')
else:
    print('erro')
