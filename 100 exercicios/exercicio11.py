nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if idade <= 2:
    print(f'{nome} está com {idade} e pela tabela é considerado bebê')
elif idade >= 3 and idade <= 11:
    print(f'{nome} está com {idade} e pela tabela é considerado criança')
elif idade >= 12 and idade <= 21:
    print(f'{nome} está com {idade} e pela tabela é considerado jovem')
elif idade >= 22 and idade <= 64:
    print(f'{nome} está com {idade} e pela tabela é considerado adulto')
elif idade >= 65 and idade <= 100:
    print(f'{nome} está com {idade} e pela tabela é considerado idoso')
else:
    print(f'{nome} está com {idade} e pela tabela é considerado muito velinho')