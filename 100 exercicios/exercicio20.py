ano = int(input('Digite um ano para ver se é ano bissexto: '))
if ano %4 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
    