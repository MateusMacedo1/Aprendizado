try:
    par = 0
    impar = 0

    for i in range(10):
        numero = int(input("Digite um número inteiro: "))
        
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

    print(f'números pares: {par}')
    print(f'números ímpares: {impar}')

except ValueError:
    print('Valor incorreto')