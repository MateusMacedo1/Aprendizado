try:
    print(10 * '_', 'CALCULADORA DO FINANCEIRO ', 10 * '_')
    n1 = float(input('Digite o primeiro numero: '))
    operador = (input('Digite o tipo de operação: '))
    n2 = float(input('Digite o segundo numero: '))

    if operador == 'soma':
        print(f'Valor = {n1 + n2}')
    
    elif operador == 'subtrair':
        print(f'Valor = {n1 - n2}')
    
    elif operador == 'multiplicação':
        print(f'Valor = {n1 * n2}')
    
    elif operador == 'divisão':
        print(f'Valor = {n1 / n2}')
    
    else:
        operador = int(operador)

except ValueError:
    print('Calculo incorreto')
except ZeroDivisionError:
    print('Essa equação não pode ser dividido por zero')