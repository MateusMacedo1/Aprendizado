#Leia um número de 0 a 7 e informe qual dia da semana representa e se é dia útil ou fim de semana.
dia = int(input('Digite um numero de 0 a 7 para saber o dia da sequencia: '))

if dia == 0 and dia == 1: #não consegui fazer diferente disso (joguei pro chaptenelson ele muda pra 6 o 7 ksksks)
    print('Domingo (fim de semana)')
elif dia == 2:
    print('Segunda (dia útil)')
elif dia == 3:
    print('Terça (dia útil)')
elif dia == 4:
    print('Quarta (dia útil)')
elif dia == 5:
    print('Quinta (dia útil)')
elif dia == 6:
    print('Sexta (dia útil)')
elif dia == 7:
    print('Sábado (fim de semana)')
else:
    print('digitou errado')