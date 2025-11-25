print('-' *40)
print('Informações')
print('-' *40)

nome = input('Digite o nome do Aluno: ')
disc = input('Digite a disciolina: ')
pv1 = float(input('Digite a nota da primeira prova: '))
pv2 = float(input('Digite a nota da segunda prova: '))
pv3 = float(input('Digite a nota da terceira prova: '))
notas = pv1 + pv2 + pv3
media = notas /3
print('-' *40)

if media >= 6.0:
    print('APROVADO')
else:
    print('REPROVADO')
