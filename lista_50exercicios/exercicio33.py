#Leia uma sigla de estado civil (S, C, D, V) e exiba o estado civil correspondente, ou informe se for inválido.

estado_civil = input('Digite o estado civil (S, C, D, V): ').upper()

if estado_civil == 'S':
    print('Solteiro(a)')

elif estado_civil == 'C':
    print('Casado(a)')

elif estado_civil == 'D':
    print('Divorciado(a)')

elif estado_civil == 'V':
    print('Viúvo(a)')

else:
    print('Erro: Sigla inválida!')