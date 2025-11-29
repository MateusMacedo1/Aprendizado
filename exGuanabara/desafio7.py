nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) /2
print(f'Sua média foi de {média:.1f}')
if média < 6:
    print('Reprovado')
else:
    print('Aprovado')