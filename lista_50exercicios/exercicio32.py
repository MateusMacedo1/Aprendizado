#Leia um número de 1 a 12 e exiba o nome do mês e a estação do ano correspondente.
mes = int(input('Digite um numero que representa um mês: '))
if mes == 1:
    print(f'o numero {mes} representa Janeiro que é Verão ')
elif mes == 2:
    print(f'o numero {mes} representa Fevereiro que é Verão')
elif mes == 3:
    print(f'o numero {mes} representa Março que é Outono')
elif mes == 4:
    print(f'o numero {mes} representa Abril que é Outono')
elif mes == 5:
    print(f'o numero {mes} representa Maio que é Outono')
elif mes == 6:
    print(f'o numero {mes} representa Junho que é Inverno')
elif mes == 7:
    print(f'o numero {mes} representa Julho que é Inverno')
elif mes == 8:
    print(f'o numero {mes} representa Agosto que é Inverno')
elif mes == 9:
    print(f'o numero {mes} representa setembro que é Primavera')
elif mes == 10:
    print(f'o numero {mes} representa Outubro que é Primavera')
elif mes == 11:
    print(f'o numero {mes} representa novembro que é Primavera')
elif mes == 12:
    print(f'o numero {mes} representa Dezembro que é Verão')
else:
    print(f'o numero {mes} não representa nenhum mes que faça parte de alguma estação')