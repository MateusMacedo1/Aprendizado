# Crie um arquivo com funções matemáticas simples e importe esse arquivo em outro programa usando um apelido.
# Utilize esse apelido para chamar as funções.

import ex11operacoes as e11

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

resultado_soma = e11.soma(a, b)
print(f'A soma é: {resultado_soma}')

resultado_subtrair = e11.subtrair(a, b)
print(f'A subtração é: {resultado_subtrair}')