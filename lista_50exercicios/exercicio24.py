# Leia cinco notas e armazene em uma lista. Exiba as notas, a média e as notas acima da média.

notas = []

for i in range(5):
    valor = float(input(f'Digite uma nota: '))
    notas.append(valor)

print(f'Suas notas: {notas}')

media = sum(notas) / 5
print(f'Média calculada: {media:.1f}')

print('Notas acima da média:')

for nota in notas:
    if nota > media:
        print(nota)