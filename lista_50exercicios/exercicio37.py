#Leia um número inteiro e exiba o resultado da divisão de 100 por esse número,
# tratando o caso de divisão por zero ou entrada inválida.

try:
    numero = int(input('Digite um número inteiro: '))
    
    resultado = 100 / numero
    
    print(f'Resultado: 100 dividido por {numero} é {resultado:.2f}')

except ValueError:
    print('Erro: Você não digitou um número inteiro válido!')

except ZeroDivisionError:
    print('Erro: Não existe divisão por zero!')