import ex9operacoes as ex9

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
operador = input('Digite o operador +, -, * e /: ')
if operador == '+':
    resultado = ex9.somar(n1, n2)
    print(f'O resultado: {resultado}')
elif operador == '-':
    resultado = ex9.subtrair(n1, n2)
    print(f'O resultado: {resultado}')
if operador == '*':
    resultado = ex9.multiplicar(n1, n2)
    print(f'O resultado: {resultado}')
elif operador == '/':
    resultado = ex9.dividir(n1, n2)
    print(f'O resultado: {resultado}')
else:
    print('Operador inexistente')