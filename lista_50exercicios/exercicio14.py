# Leia duas notas e a quantidade de faltas de um aluno
# e determine sua situação escolar considerando média e frequência.

try:
    n1 = float(input('Digite uma nota: '))
    n2 = float(input('Digite uma nota: '))
    ft = int(input('Digite as faltas: '))

    media = (n1 + n2) / 2

    if media >= 0 and media < 6 and ft > 0:
        print('Sua média é ruim e sua frequencia é baixa')
    elif media >= 0 and media < 6 and ft == 0:
        print('Sua média é ruim e sua frequencia é boa')
    elif media > 5 and media <= 10 and ft == 0:
        print('Sua média é boa e sua frequencia é boa')
    elif media > 5 and media <= 10 and ft > 0:
        print('Sua média é boa mas sua frequencia é baixa')
    else:
        print('Valores inválidos')
except ValueError:
        print('Valores inválidos')  
except Exception:
        print('Valores inválidos')