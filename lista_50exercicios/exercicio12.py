#Leia um caractere e informe se ele é letra maiúscula, minúscula, dígito ou outro símbolo.
caracter = input('Digite algo: ')

if caracter.isupper():
    print('Letra maiuscula')
elif caracter.islower():
    print('Letra minuscula')
elif not caracter.isalnum():
    print('É simbolo especial')
elif not caracter.isdigit():
    print('É um digito')
else:
    print('Erro')