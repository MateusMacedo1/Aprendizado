# Leia duas notas e a quantidade de faltas de um aluno e determine sua situação escolar considerando média e frequência.
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma nota: '))
ft = int(input('Digite as faltas: '))

if n1 < 0 and n2 < 0:
    print(f'A media do aluno é {2 / (n1 + n2)} e sua frequencia é {ft}')