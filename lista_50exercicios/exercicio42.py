# Leia uma expressão aritmética simples digitada como texto, avalie e exiba o resultado, tratando expressões inválidas.

expressão = input('Digite uma conta (ex: 10 + 5 * 2): ')

try:
    resultado = eval(expressão)
    print(f'O resultado é: {resultado}')

except ZeroDivisionError:
    print('Erro: Impossível dividir por zero.')

except SyntaxError:
    print('Erro: A sintaxe da conta está errada.')

except NameError:
    print('Erro: Não use palavras, apenas números e operadores.')