nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade <= 2:
    print(f'{nome} está com {idade} e pela tabela é considerado bebê')
elif idade >= 3 and idade <= 11:
    tipo = 'criança'
elif idade >= 12 and idade <= 21:
    tipo = 'jovem'
elif idade >= 22 and idade <= 64:
    tipo = 'adulto'
elif idade >= 65 and idade <= 100:
    tipo = 'idoso'
else:
    tipo = 'muito velinho'
    print(f'{nome} está com {idade} e pela tabela é considerado {tipo}')