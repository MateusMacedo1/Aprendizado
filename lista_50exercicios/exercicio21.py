# Leia uma frase e exiba a quantidade de caracteres, a quantidade de espaços e a quantidade de vogais.

try:
    text = []
    for i in range(1):
        frase = str(input('Digite uma frase: '))
        text.append(frase)

    if text:
        caracter = max(text)
        quantidade_espacos = frase.count(' ')
        vogais = "aeiou"
        total_vogais = sum(frase.lower().count(vogal) for vogal in vogais)
        print(f'A frase: {caracter}; possui {len(caracter)} caracteres')
        print(f"O texto possui {quantidade_espacos} espaços.")
        print(f"A frase tem {total_vogais} vogais.")


    else:
        print('Frase não digitada')

except ValueError:
    print('Valor incorreto')