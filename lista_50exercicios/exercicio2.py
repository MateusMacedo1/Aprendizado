# Leia três números reais e determine qual deles é o maior.
# Em caso de igualdade, informe adequadamente.
try:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite mais um numero: '))
    num3 = int(input('Digite outro numero: '))

    resultado = max(num1, num2, num3)
    if num1 == num2 == num3:
        print('São Numeros iguais')
    else:
        print(f' Numero maior é: {resultado}')

except ValueError:
    print('ERRO')