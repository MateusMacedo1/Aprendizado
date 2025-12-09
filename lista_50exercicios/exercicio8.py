# Leia um número de 1 a 12 representando um mês
# e informe o nome do mês correspondente e o trimestre do ano ao qual pertence.
try:
    mes = int(input('Digite um numero que representa um mês: '))
    if mes == 1:
        print(f'o numero {mes} representa Janeiro que faz parte do 1º semestre')
    elif mes == 2:
        print(f'o numero {mes} representa Fevereiro que faz parte do 1º semestre')
    elif mes == 3:
        print(f'o numero {mes} representa Março que faz parte do 1º semestre')
    elif mes == 4:
        print(f'o numero {mes} representa Abril que faz parte do 2º semestre')
    elif mes == 5:
        print(f'o numero {mes} representa Maio que faz parte do 2º semestre')
    elif mes == 6:
        print(f'o numero {mes} representa Junho que faz parte do 2º semestre')
    elif mes == 7:
        print(f'o numero {mes} representa Julho que faz parte do 3º semestre')
    elif mes == 8:
        print(f'o numero {mes} representa Agosto que faz parte do 3º semestre')
    elif mes == 9:
        print(f'o numero {mes} representa setembro que faz parte do 3º semestre')
    elif mes == 10:
        print(f'o numero {mes} representa Outubro que faz parte do 4º semestre')
    elif mes == 11:
        print(f'o numero {mes} representa novembro que faz parte do 4º semestre')
    elif mes == 12:
        print(f'o numero {mes} representa Dezembro que faz parte do 4º semestre')
    else:
        print(f'o numero {mes} não representa nenhum mes que faça parte de algum semestre')
except ValueError:
    print('Apenas numeros')