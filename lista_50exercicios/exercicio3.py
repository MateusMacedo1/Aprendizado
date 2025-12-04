# Leia a nota final de um aluno e classifique-o como aprovado,
# recuperação ou reprovado, conforme a faixa de valores permitida.
try:

    nota = float(input('Digite a nota do aluno: '))
    if nota >= 0 and nota <= 5:
        print('Reprovado')
    elif nota >= 7 and nota <= 10:
        print('Aprovado')
    elif nota == 6:
        print('Recuperação')
    else:
        print('Valor Inválido')

except ValueError:
    print('ERRO')